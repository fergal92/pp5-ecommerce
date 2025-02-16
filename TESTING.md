# Testing Documentation for Doggo Down Under

This document outlines the testing results for various features of the **Doggo Down Under** e-commerce website.

---

## **Table of Contents**
1. [Navigation](#navigation)  
2. [Search Functionality](#search-functionality)  
3. [Wishlist](#wishlist)  
4. [Shopping Bag & Checkout](#shopping-bag--checkout)  
5. [Payment (Stripe Integration)](#payment-stripe-integration)  
6. [Newsletter Subscription](#newsletter-subscription)  
7. [Product Management (Admin)](#product-management-admin)  
8. [Footer Links](#footer-links)  
9. [Responsiveness & Mobile Testing](#responsiveness--mobile-testing)  
10. [Performance & Security](#performance--security)  

---

## **Navigation**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Click on the **logo** | Redirects to the homepage | ✅ | Pass |
| Click on **Products** in navbar | Redirects to the products page | ✅ | Pass |
| Click on **Wishlist** | Redirects to wishlist page | ✅ | Pass |
| Click on **Shopping Bag** | Redirects to shopping bag page | ✅ | Pass |
| Click on **Checkout** | Redirects to checkout page | ✅ | Pass |

---

## **Search Functionality**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Enter a valid product name | Displays matching products | ✅ | Pass |
| Enter a partial product name | Displays relevant suggestions | ✅ | Pass |
| Enter gibberish text | Shows "No products found" message | ✅ | Pass |
| Search with an empty input | No search results displayed | ✅ | Pass |

---

## **Wishlist**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Add a product to the wishlist | Product appears in wishlist | ✅ | Pass |
| Remove a product from the wishlist | Product disappears from wishlist | ✅ | Pass |
| Click on a product in wishlist | Redirects to product page | ✅ | Pass |

---

## **Shopping Bag & Checkout**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Add product to bag | Product appears in shopping bag | ✅ | Pass |
| Remove product from bag | Product is removed from shopping bag | ✅ | Pass |
| Update quantity in shopping bag | Quantity updates correctly | ✅ | Pass |
| Click "Proceed to Checkout" | Redirects to checkout page | ✅ | Pass |

---

## **Payment (Stripe Integration)**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Enter valid card details | Payment is processed successfully | ✅ | Pass |
| Enter invalid card details | Displays error message | ✅ | Pass |
| Use expired card | Displays error message | ✅ | Pass |
| Successful transaction | Order confirmation page appears | ✅ | Pass |

---

## **Newsletter Subscription**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Enter valid email & submit | Subscription success message | ✅ | Pass |
| Enter invalid email format | Error message displayed | ✅ | Pass |
| Try subscribing twice with the same email | Displays "Already subscribed" message | ✅ | Pass |

---

## **Product Management (Admin)**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Admin logs in | Redirects to admin panel | ✅ | Pass |
| Admin adds a new product | Product appears in store | ✅ | Pass |
| Admin edits a product | Updated details reflect on product page | ✅ | Pass |
| Admin deletes a product | Product is removed from store | ✅ | Pass |

---

## **Footer Links**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Click on **Facebook link** | Redirects to Facebook page | ✅ | Pass |
| Click on **Charity link** | Redirects to external website | ✅ | Pass |

---

## **Responsiveness & Mobile Testing**
| Device | Expected Result | Actual Result | Pass/Fail |
|--------|---------------|--------------|----------|
| **Mobile (iPhone, Android)** | Navbar collapses, site adapts to screen size | ✅ | Pass |
| **Tablet (iPad, Galaxy Tab)** | Content scales properly | ✅ | Pass |
| **Desktop** | Full layout is displayed properly | ✅ | Pass |

---

## **Performance & Security**
| Test Case | Expected Result | Actual Result | Pass/Fail |
|-----------|---------------|--------------|----------|
| Page Load Speed | Loads within 3 seconds | ✅ | Pass |
| User Data Encryption | Stripe uses HTTPS & secure transactions | ✅ | Pass |
| CSRF Protection | Forms include CSRF tokens | ✅ | Pass |
| SQL Injection Prevention | Special characters in inputs do not break database | ✅ | Pass |

---

## **Final Notes**
- All tests **PASSED** successfully.  
- The website is fully functional across desktop, tablet, and mobile devices.  
- Performance is optimized, and all security checks are in place.  

---

End of testing report.
