# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files and used the [Validate by uri](https://validator.w3.org/#validate_by_uri) for the live pages.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2F) | ![screenshot](documentation/html-validation-home.png) | Pass: No Errors|
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/html-validation-about.png) | Pass: No Errors |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2F%3Fsort%3Dprice%26direction%3Dasc) | ![screenshot](documentation/html-validation-products.png) | Warning (2): section lacks headings |
| Product Details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2Fproduct_detail%2F15%2F) | ![screenshot](documentation/html-validation-product-details.png) | Warning (1): section lacks headings |
| Add Product | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2Fadd%2F) | ![screenshot](documentation/html-validation-add-product.png) | Pass: No Errors |
| Edit Product | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fproducts%2Fedit%2F15%2F) | ![screenshot](documentation/html-validation-edit-product.png) | Pass: No Errors |
| FAQs | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Ffaqs%2F) | ![screenshot](documentation/html-validation-faqs.png) | Pass: No Errors |
| Bespoke | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fbespoke%2F) | ![screenshot](documentation/html-validation-bespoke.png) | Pass: No Errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/html-validation-contact.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fbag%2F) | ![screenshot](documentation/html-validation-bag.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fcheckout%2F) | ![screenshot](documentation/html-validation-checkout.png) | Warning (2): section lacks headings |
| Checkout Success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fcheckout%2Fcheckout_success%2FAE806850B71840C693B8FF6921505B95) | ![screenshot](documentation/html-validation-checkout-success.png) |  |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2Fprofile%2F) | ![screenshot](documentation/html-validation-profile.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fnyreewaters-art-ccb67c4ebd7f.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/css-validation-base.png) | Pass: No Errors |
| checkout.css | n/a | ![screenshot](documentation/css-validation-checkout.png) | Pass: No Errors |
| profile.css | n/a | ![screenshot](documentation/css-validation-profiles.png) | Pass: No Errors |
| home-about.css | n/a | ![screenshot](documentation/css-validation-home-about.png) | Pass: No Errors |
| faq.css | n/a | ![screenshot](documentation/css-validation-faqs.png) | Pass: No Errors |
| contact.css | n/a | ![screenshot](documentation/css-validation-contact.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/js-validation-stripe.png) | Undefined Stripe variable - external library |
| countryfield.js | ![screenshot](documentation/js-validation-countryfield.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Bag urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-urls.png) | Pass: No Errors |
| Bag views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-views.png) | Pass: No Errors |
| Bag apps.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-apps.png) | Pass: No Errors |
| Bag bagtools.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-bagtools.png) | Pass: No Errors |
| Bag contexts.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-bag-contexts.png) | Pass: No Errors |
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
| Home urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-home-urls.png) | Pass: No Errors |
| Home views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-home-views.png) | Pass: No Errors |
| nyreewaters_art settings.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-nyreewaters_art-settings.png) | Pass: No Errors (#noqa added for long host URL and django names) |
| nyreewaters_art urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-nyreewaters_art-urls.png) | Pass: No Errors |
| nyreewaters_art views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-nyreewaters_art-views.png) | Pass: No Errors |
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
| Contact froms.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-forms.png) | Pass: No Errors |
| Contact models.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-models.png) | Pass: No Errors |
| Contact urls.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-urls.png) | Pass: No Errors |
| Contact views.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-contact-views.png) | Pass: No Errors |
| Root Level custom_storages.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-root-custom_storages.png) | Pass: No Errors |
| Root Level manage.py | [PEP8 CI](#) | ![screenshot](documentation/py-validation-root-manage.png) | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.
The browsers tested include:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

| Browser | Home | Products | FAQs | Newsletter | Which Scent? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-products.png) | ![screenshot](documentation/browser-chrome-faqs.png) | ![screenshot](documentation/browser-chrome-bespoke.png) | ![screenshot](documentation/browser-chrome-about.png) |Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-products.png) | ![screenshot](documentation/browser-firefox-faqs.png) | ![screenshot](documentation/browser-firefox-bespoke.png) | ![screenshot](documentation/browser-firefox-about.png) |Works as expected |
| Edge | ![screenshot](documentation/browser-edge-home.png) | ![screenshot](documentation/browser-edge-products.png) | ![screenshot](documentation/browser-edge-faqs.png) | ![screenshot](documentation/browser-edge-bespoke.png) | ![screenshot](documentation/browser-edge-about.png) |Works as expected |
| Safari | ![screenshot](documentation/browser-safari-home.png) | ![screenshot](documentation/browser-safari-products.png) | ![screenshot](documentation/browser-safari-faqs.png) | ![screenshot](documentation/browser-safari-bespoke.png) | ![screenshot](documentation/browser-safari-about.png) |Minor CSS differences |
| Brave | ![screenshot](documentation/browser-brave-home.png) | ![screenshot](documentation/browser-brave-products.png) | ![screenshot](documentation/browser-brave-faqs.png) | ![screenshot](documentation/browser-brave-bespoke.png) | ![screenshot](documentation/browser-brave-about.png) |Works as expected |
| Opera | ![screenshot](documentation/browser-opera-home.png) | ![screenshot](documentation/browser-opera-products.png) | ![screenshot](documentation/browser-opera-faqs.png) | ![screenshot](documentation/browser-opera-bespoke.png) | ![screenshot](documentation/browser-opera-about.png) |Minor differences |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Products | FAQs | Newsletter | Which Scent | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools - Samsung Galaxy S20 Ultra) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-products.png) | ![screenshot](documentation/responsive-mobile-faqs.png) | ![screenshot](documentation/responsive-mobile-about.png) |![screenshot](documentation/responsive-mobile-bespoke.png) | Works as expected |
| Tablet (iPad Air) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-products.png) | ![screenshot](documentation/responsive-tablet-faqs.png) | ![screenshot](documentation/responsive-tablet-about.png) | ![screenshot](documentation/responsive-tablet-bespoke.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-products.png) | ![screenshot](documentation/responsive-desktop-faqs.png) | ![screenshot](documentation/responsive-desktop-about.png) |![screenshot](documentation/responsive-tablet-bespoke.png) |  Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl-home.png) | ![screenshot](documentation/responsive-xl-products.png) | ![screenshot](documentation/responsive-xl-faqs.png) | ![screenshot](documentation/responsive-xl-about.png) | ![screenshot](documentation/responsive-xl-bespoke.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsive-4k-home.png) | ![screenshot](documentation/responsive-4k-products.png) | ![screenshot](documentation/responsive-4k-faqs.png) | ![screenshot](documentation/responsive-4k-about.png) | ![screenshot](documentation/responsive-4k-bespoke.png) | Noticeable scaling issues |
| iPhone XS | ![screenshot](documentation/responsive-iphone-home.png) | ![screenshot](documentation/responsive-iphone-products.png) | ![screenshot](documentation/responsive-iphone-faqs.png) | ![screenshot](documentation/responsive-iphone-about.png) | ![screenshot](documentation/responsive-iphone-bespoke.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Slow response time due to large images |
| About | ![screenshot](documentation/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse-about-desktop.png) | Slow response time due to large images |
| Products | ![screenshot](documentation/lighthouse-products-mobile.png) | ![screenshot](documentation/lighthouse-products-desktop.png) | Slow response time due to large images |
| FAQs | ![screenshot](documentation/lighthouse-faqs-mobile.png) | ![screenshot](documentation/lighthouse-faqs-desktop.png) | Slow response time due to large images |
| Bespoke | ![screenshot](documentation/lighthouse-bespoke-mobile.png) | ![screenshot](documentation/lighthouse-bespoke-desktop.png) | Slow response time due to large images |
| Contact | ![screenshot](documentation/lighthouse-contact-mobile.png) | ![screenshot](documentation/lighthouse-contact-desktop.png) | Slow response time due to large images |
| Bag | ![screenshot](documentation/lighthouse-bag-mobile.png) | ![screenshot](documentation/lighthouse-bag-desktop.png) | Slow response time due to large images |
| Checkout | ![screenshot](documentation/lighthouse-checkout-mobile.png) | ![screenshot](documentation/lighthouse-checkout-desktop.png) | Slow response time due to large images |
| Checkout Success | ![screenshot](documentation/lighthouse-checkout-success-mobile.png) | ![screenshot](documentation/lighthouse-checkout-success-desktop.png) | Slow response time due to large images |