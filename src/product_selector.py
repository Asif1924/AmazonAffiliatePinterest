"""
Product selection logic
"""

import datetime as dt
import logging
import random
from typing import List, Any

logger = logging.getLogger(__name__)


class ProductSelector:
    """Selects products for daily CSV generation"""
    
    def __init__(self, cooldown_days: int, min_ready_products: int):
        """
        Initialize product selector
        
        Args:
            cooldown_days: Days to wait before reusing a product
            min_ready_products: Minimum READY products required
        """
        self.cooldown_days = cooldown_days
        self.min_ready_products = min_ready_products
    
    def _parse_date(self, date_str: str) -> dt.date:
        """Parse date string to date object"""
        if not date_str:
            return None
        try:
            return dt.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return None
    
    def _is_eligible(self, product: Any) -> bool:
        """
        Check if product is eligible for selection
        
        Args:
            product: Product object
        
        Returns:
            True if eligible, False otherwise
        """
        # Must be READY status
        if product.status != "READY":
            return False
        
        # Check cooldown period
        last_used = self._parse_date(product.last_used_date)
        if last_used:
            days_since = (dt.date.today() - last_used).days
            if days_since < self.cooldown_days:
                logger.debug(
                    f"Product {product.product_id} in cooldown "
                    f"({days_since}/{self.cooldown_days} days)"
                )
                return False
        
        return True
    
    def _weighted_sample(self, products: List[Any], k: int) -> List[Any]:
        """
        Select k products using weighted random sampling based on priority
        
        Args:
            products: List of eligible products
            k: Number of products to select
        
        Returns:
            List of selected products
        """
        if len(products) <= k:
            return products
        
        # Weight by priority (1-5, higher = more likely)
        weights = [max(1, p.priority) for p in products]
        
        # Sample without replacement
        chosen = []
        pool = products[:]
        pool_weights = weights[:]
        
        for _ in range(k):
            if not pool:
                break
            
            # Weighted random choice
            pick = random.choices(pool, weights=pool_weights, k=1)[0]
            idx = pool.index(pick)
            
            chosen.append(pick)
            pool.pop(idx)
            pool_weights.pop(idx)
        
        return chosen
    
    def select_products(self, products: List[Any], count: int) -> List[Any]:
        """
        Select products for today's CSV
        
        Args:
            products: All products from Google Sheets
            count: Number of products to select
        
        Returns:
            List of selected products
        
        Raises:
            RuntimeError: If not enough eligible products
        """
        # Filter eligible products
        eligible = [p for p in products if self._is_eligible(p)]
        
        logger.info(f"Found {len(eligible)} eligible products (READY + not in cooldown)")
        
        # Check minimum requirement
        if len(eligible) < self.min_ready_products:
            raise RuntimeError(
                f"Not enough eligible products. Found {len(eligible)}, "
                f"need at least {self.min_ready_products}. "
                "Please add more READY products or reduce COOLDOWN_DAYS."
            )
        
        if len(eligible) < count:
            logger.warning(
                f"Only {len(eligible)} eligible products available, "
                f"requested {count}. Selecting all eligible."
            )
            return eligible
        
        # Select using weighted sampling
        selected = self._weighted_sample(eligible, count)
        
        return selected

