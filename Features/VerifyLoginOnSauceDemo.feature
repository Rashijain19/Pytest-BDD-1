Feature:Verify Login functionality

#  - The following things are performed in this test
#  - Login as User
#  - Verify product listing page
#  - Select Add to Cart
#  - Go to Your Cart page
#  - Verify Checkout and Finish Functionality
#  - Verify return to home page Functionality
#  - Verify Logout page

Scenario: VerifyLoginFeatureForUser

  Given Login on SauceLab Page Open

  #@when(parsers.parse('Login with"{username}""{password}"'))
  When Login with "standard_user" and "secret_sauce"
  Then User lands on Sauce Demo Product Page
#  #@when(parsers.parse('Click on Add to Cart button"{select_cart}"'))
#  When Select asset type "add to cart" on product page
#  #@then(parsers.parse('item added successfully in cart"{remove_cart}"'))
#  Then Go to Cart page
#  #@when(parsers.parse('click on checkout button{checkout_item}'))
#  When Click on Checkout button
#  And Fill your Information - Your First Name, Last Name and Pincode
#  #@when(parsers.parse('click on checkout button"{continue_checkout}"'))
#  When Click on Checkout button
#  #@then(parsers.parse('click on Finish button"{finish_checkout}"'))
#  Then Click on Finish button and Checkout Successfully Completed..!!
#  #@then(parsers.parse('Go to Back Home page redirects to main product page"{Back_home_page}"'))
#  Then click on Back Home page to return to product page
