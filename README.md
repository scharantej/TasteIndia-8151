## Flask Application Design

### HTML Files

- **index.html**: This is the landing page of your application. It should include a title, a brief description of the app, and a call-to-action button that prompts users to download the app.
- **snacks.html**: This page displays the list of available snacks, along with their prices and descriptions. It should also include a form that allows users to add snacks to their cart.
- **cart.html**: This page displays the items in the user's cart, along with the total cost. It should also include a checkout button.
- **checkout.html**: This page collects the user's shipping and payment information.

### Routes

- `/`: This route handles the landing page. It should render the `index.html` file.
- `/snacks`: This route handles the snacks page. It should render the `snacks.html` file, passing in a list of snacks as a context variable.
- `/cart`: This route handles the cart page. It should render the `cart.html` file, passing in the user's cart as a context variable.
- `/checkout`: This route handles the checkout page. It should render the `checkout.html` file, passing in the user's cart as a context variable.
- `/place-order`: This route handles the order placement. It should collect the user's shipping and payment information and place the order.