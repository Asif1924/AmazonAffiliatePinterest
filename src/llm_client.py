"""
LLM client for generating CSV content
"""

import logging
import time
from typing import Optional

import config

logger = logging.getLogger(__name__)


class LLMClient:
    """Client for calling various LLM providers"""
    
    def __init__(self, provider: str):
        """
        Initialize LLM client
        
        Args:
            provider: LLM provider name (openai, anthropic, google, openrouter)
        """
        self.provider = provider.lower()
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the appropriate LLM client"""
        if self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=config.OPENAI_API_KEY)
            self.model = config.OPENAI_MODEL
            
        elif self.provider == "anthropic":
            from anthropic import Anthropic
            self.client = Anthropic(api_key=config.ANTHROPIC_API_KEY)
            self.model = config.ANTHROPIC_MODEL
            
        elif self.provider == "google":
            import google.generativeai as genai
            genai.configure(api_key=config.GOOGLE_API_KEY)
            self.client = genai
            self.model = config.GOOGLE_MODEL
            
        elif self.provider == "openrouter":
            from openai import OpenAI
            self.client = OpenAI(
                api_key=config.OPENROUTER_API_KEY,
                base_url="https://openrouter.ai/api/v1"
            )
            self.model = config.OPENROUTER_MODEL
            
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")
        
        logger.info(f"Initialized {self.provider} client with model {self.model}")
    
    def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=config.LLM_TEMPERATURE,
            max_tokens=config.LLM_MAX_TOKENS,
            timeout=config.LLM_TIMEOUT
        )
        return response.choices[0].message.content.strip()
    
    def _call_anthropic(self, prompt: str) -> str:
        """Call Anthropic API"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=config.LLM_MAX_TOKENS,
            temperature=config.LLM_TEMPERATURE,
            messages=[
                {"role": "user", "content": prompt}
            ],
            timeout=config.LLM_TIMEOUT
        )
        return response.content[0].text.strip()
    
    def _call_google(self, prompt: str) -> str:
        """Call Google Gemini API"""
        model = self.client.GenerativeModel(self.model)
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': config.LLM_TEMPERATURE,
                'max_output_tokens': config.LLM_MAX_TOKENS,
            }
        )
        return response.text.strip()
    
    def generate_csv(self, prompt: str) -> str:
        """
        Generate CSV content using LLM
        
        Args:
            prompt: Complete prompt with product data
        
        Returns:
            CSV text from LLM
        
        Raises:
            Exception: If API call fails after retries
        """
        for attempt in range(1, config.API_RETRY_ATTEMPTS + 1):
            try:
                logger.info(f"Calling {self.provider} API (attempt {attempt}/{config.API_RETRY_ATTEMPTS})")
                
                if self.provider in ["openai", "openrouter"]:
                    result = self._call_openai(prompt)
                elif self.provider == "anthropic":
                    result = self._call_anthropic(prompt)
                elif self.provider == "google":
                    result = self._call_google(prompt)
                else:
                    raise ValueError(f"Unsupported provider: {self.provider}")
                
                # Clean up response (remove markdown code blocks if present)
                result = self._clean_response(result)
                
                logger.info(f"Successfully received response from {self.provider}")
                return result
                
            except Exception as e:
                logger.warning(f"Attempt {attempt} failed: {e}")
                
                if attempt < config.API_RETRY_ATTEMPTS:
                    logger.info(f"Retrying in {config.API_RETRY_DELAY} seconds...")
                    time.sleep(config.API_RETRY_DELAY)
                else:
                    logger.error(f"All {config.API_RETRY_ATTEMPTS} attempts failed")
                    raise
    
    def _clean_response(self, text: str) -> str:
        """
        Clean LLM response to extract pure CSV
        
        Args:
            text: Raw LLM response
        
        Returns:
            Cleaned CSV text
        """
        # Remove markdown code blocks
        if "```" in text:
            # Extract content between ```csv and ``` or just between ```
            lines = text.split("\n")
            in_code_block = False
            csv_lines = []
            
            for line in lines:
                if line.strip().startswith("```"):
                    in_code_block = not in_code_block
                    continue
                if in_code_block or (not any(line.strip().startswith(x) for x in ["```", "#", "Here"])):
                    csv_lines.append(line)
            
            text = "\n".join(csv_lines)
        
        return text.strip()

