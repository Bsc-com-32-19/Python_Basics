import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# other way of importing the module
from ecommerce import shipping
shipping.calc_shipping()

# to import specific function

from ecommerce.shipping import calc_shipping
shipping.calc_shipping()