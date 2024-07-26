# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files and used the [Validate by uri](https://validator.w3.org/#validate_by_uri) for the live pages.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2F) | ![screenshot](documentation/readme/html-validation-home.png) | Pass: No Errors|
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/readme/html-validation-about.png) | Pass: No Errors |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2F%3Fsort%3Dprice%26direction%3Dasc) | ![screenshot](documentation/readme/html-validation-products.png) | Warning (2): section lacks headings |
| Product Details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2Fproduct_detail%2F15%2F) | ![screenshot](documentation/readme/html-validation-product-details.png) | Warning (1): section lacks headings |
| Add Product | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2Fadd%2F) | ![screenshot](documentation/readme/html-validation-add-product.png) | Pass: No Errors |
| Edit Product | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2Fedit%2F15%2F) | ![screenshot](documentation/readme/html-validation-edit-product.png) | Pass: No Errors |
| FAQs | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Ffaqs%2F) | ![screenshot](documentation/readme/html-validation-faqs.png) | Pass: No Errors |
| Bespoke | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fbespoke%2F) | ![screenshot](documentation/readme/html-validation-bespoke.png) | Pass: No Errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/readme/html-validation-contact.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fbag%2F) | ![screenshot](documentation/readme/html-validation-bag.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fcheckout%2F) | ![screenshot](documentation/readme/html-validation-checkout.png) | Warning (2): section lacks headings |
| Checkout Success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fcheckout%2Fcheckout_success%2FAE806850B71840C693B8FF6921505B95) | ![screenshot](documentation/readme/html-validation-checkoutsuccess.png) |  |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fprofile%2F) | ![screenshot](documentation/readme/html-validation-profile.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [Jigsaw](#) | ![screenshot](documentation/readme/css-validation-base.png) | Pass: No Errors |
| checkout.css | n/a | ![screenshot](documentation/readme/css-validation-checkout.png) | Pass: No Errors |
| profile.css | n/a | ![screenshot](documentation/readme/css-validation-profiles.png) | Pass: No Errors |
| home-about.css | n/a | ![screenshot](documentation/css-validation-home-about.png) | Pass: No Errors |
| faq.css | n/a | ![screenshot](documentation/readme/css-validation-faqs.png) | Pass: No Errors |
| contact.css | n/a | ![screenshot](documentation/readme/css-validation-contact.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/readme/js-validation-stripe.png) | Undefined Stripe variable - external library |
| countryfield.js | ![screenshot](documentation/readme/js-validation-countryfield.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Bag urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-urls.png) | Pass: No Errors |
| Bag views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-views.png) | Pass: No Errors |
| Bag apps.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-apps.png) | Pass: No Errors |
| Bag bagtools.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-bagtools.png) | Pass: No Errors |
| Checkout admin.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-admin.png) | Pass: No Errors |
| Checkout forms.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-forms.png) | Pass: No Errors |
| Checkout models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-models.png) | Pass: No Errors |
| Checkout signals.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-signals.png) | Pass: No Errors |
| Checkout urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-urls.png) | Pass: No Errors |
| Checkout views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-views.png) | Pass: No Errors |
| Checkout webhook_handler.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-webhook_handler.png) | Pass: No Errors |
| Checkout webhooks.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-checkout-webhooks.png) | Error: Line too long |
| FAQs admin.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-faqs-admin.png) | Pass: No Errors |
| FAQs models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-faqs-models.png) | Pass: No Errors |
| FAQs urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-faqs-urls.png) | Pass: No Errors |
| FAQs views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-faqs-views.png) | Pass: No Errors |
| Home admin.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-home-admin.png) | Pass: No Errors |
| Home models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-home-models.png) | Pass: No Errors |
| Home urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-home-urls.png) | Pass: No Errors |
| Home views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-home-views.png) | Pass: No Errors |
| nyreewaters_art settings.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-nyreewaters-art-settings.png) | Pass: No Errors |
| nyreewaters_art urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-nyreewaters-art-urls.png) | Pass: No Errors |
| Bespoke admin.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bespoke-admin.png) | Pass: No Errors |
| Bespoke forms.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bespoke-forms.png) | Pass: No Errors |
| Bespoke models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bespoke-models.png) | Pass: No Errors |
| Bespoke urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bespoke-urls.png) | Pass: No Errors |
| Bespoke views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bespoke-views.png) | Pass: No Errors |
| Products admin.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-products-admin.png) | Pass: No Errors |
| Products forms.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-products-forms.png) | Pass: No Errors |
| Products models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-products-models.png) | Pass: No Errors |
| Products urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-products-urls.png) | Pass: No Errors |
| Products views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-products-views.png) | Pass: No Errors |
| Products widgets.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-products-widgets.png) | Pass: No Errors |
| Profiles forms.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-profiles-forms.png) | Pass: No Errors |
| Profiles models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-profiles-models.png) | Pass: No Errors |
| Profiles urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-profiles-urls.png) | Pass: No Errors |
| Profiles views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-profiles-views.png) | Pass: No Errors |
| Contact admin.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-admin.png) | Pass: No Errors |
| Contact models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-models.png) | Pass: No Errors |
| Contact urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-urls.png) | Pass: No Errors |
| Contact views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-views.png) | Pass: No Errors |
| Root Level custom_storages.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-rootlevel-custom_storages.png) | Pass: No Errors |
| Root Level manage.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-rootlevel-manage.png) | Pass: No Errors |
