# QuickBuy E-commerce API

QuickBuy is a robust e-commerce API built with Django and Django Rest Framework. It provides a comprehensive set of functionalities for managing products, categories, user authentication, shopping carts, and orders.

## Features

*   **Product Management:**
    *   Create, retrieve, update, and delete products.
    *   Manage product categories.
    *   Add multiple images to products.
    *   Filter products by category and price range.
    *   Search products by name, description, and category name.
    *   Order products by price.
    *   Product reviews and ratings.
*   **User Management:**
    *   Custom user model with email as the primary authentication field.
    *   User registration, login, and profile management via Djoser.
    *   Admin panel for managing users.
*   **Shopping Cart:**
    *   Create and manage shopping carts for authenticated users.
    *   Add, update, and delete items in the cart.
    *   View cart details, including total price.
*   **Order Management:**
    *   Create orders from a shopping cart.
    *   View order history.
    *   Admin can update order status (e.g., Not Paid, Ready To Ship, Shipped, Delivered, Cancelled).
    *   Users can cancel their own orders (with restrictions).
*   **API Documentation:**
    *   Interactive API documentation using Swagger UI and Redoc.
*   **Permissions:**
    *   Role-based permissions for various actions (e.g., `IsAdminOrReadOnly`, `IsReviewAuthorOrReadonly`).
*   **Database:**
    *   PostgreSQL database integration.

## Technologies Used

*   **Backend:** Django, Django Rest Framework
*   **Authentication:** Djoser, Simple JWT
*   **Database:** PostgreSQL
*   **API Documentation:** DRF-YASG (Swagger, Redoc)
*   **Filtering:** Django-Filter
*   **Development Tools:** Django Debug Toolbar

## Setup and Installation

Follow these steps to get the QuickBuy API up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/neamul602/QuickBuy.git
cd QuickBuy
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Database Setup

This project uses PostgreSQL. Ensure you have PostgreSQL installed and running.

Update the `DATABASES` setting in `quick_buy/settings.py` with your PostgreSQL credentials. The current configuration is:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quick-buy',
        'USER': 'postgres',
        'PASSWORD': '1234', # Change this to your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

### 5. Run Migrations

Apply the database migrations to create the necessary tables:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)

Create an administrator account to access the Django admin panel and manage data:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser credentials.

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

The API provides interactive documentation via Swagger UI and Redoc.

*   **Swagger UI:** `http://127.0.0.1:8000/swagger/`
*   **Redoc:** `http://127.0.0.1:8000/redoc/`

You can explore all available endpoints, their request/response schemas, and test them directly from these interfaces.

## Authentication

This API uses JWT (JSON Web Tokens) for authentication.

1.  **Obtain a JWT Token:**
    Send a POST request to `/auth/jwt/create/` with your `email` and `password` to get an access token.

    ```json
    {
        "email": "your_email@example.com",
        "password": "your_password"
    }
    ```

2.  **Include Token in Requests:**
    For authenticated endpoints, include the access token in the `Authorization` header of your requests:

    `Authorization: JWT <your_access_token>`

## Project Structure

*   `api/`: Main API application, handles URL routing and global permissions.
*   `product/`: Manages product-related functionalities (categories, products, images, reviews).
*   `order/`: Handles shopping cart and order processing.
*   `users/`: Custom user model and authentication logic.
*   `quick_buy/`: Project-level settings, URLs, and WSGI/ASGI configurations.
*   `fixtures/`: Contains initial data for the project (e.g., `product_data.json`).
*   `requirements.txt`: Lists all project dependencies.

## Contributing

Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the BSD License.
