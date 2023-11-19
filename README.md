# Shoe Store

This is a Django-based project for an online shoe store.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AibekYrysbekov/Neobis_E_Store_Project.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

## Usage

This project implements an online shoe store using Django and Django REST framework. It provides APIs to manage products, orders, and users.


## Project Structure

The project consists of the following main models:

- `UserProfile`: User model with additional fields.
- `Product`: Product (shoe) model with descriptions, prices, and images.
- `Image`: Model for product images.
- `Category`: Model for product categories.
- `Order`: Order model with products, shipping addresses, and status.

## Technologies

Key technologies and libraries used in the project:

- Django
- Django REST framework

## Contributions

We welcome everyone to contribute to the project! If you find a bug or want to make improvements, please submit a pull request.

