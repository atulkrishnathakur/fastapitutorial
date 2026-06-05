import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.product.services import (
    create_product,
    get_all_products,
    get_product,
    update_product,
    delete_product,
)
from app.product.schemas import ProductBase, ProductUpdate
from app.product.models import Product
from fastapi import HTTPException

# Service tests (Hybrid Unit/Integration Tests)
# These test individual service functions from app/product/services.py
# They are unit tests in that they focus on specific functions, but integration tests
# because they use a real SQLite database via AsyncSession
@pytest.mark.asyncio
async def test_create_product(setup_database, test_session: AsyncSession):
    """
    Hybrid unit/integration test for the create_product service function.
    - Creates a product with title "Test Product" using the test session.
    - Verifies the product is created with the correct title and a non-null ID.
    - Uses a real database, testing both function logic and database interaction.
    """
    product_data = ProductBase(title="Test Product")
    product = await create_product(test_session, product_data)
    assert product.title == "Test Product"
    assert product.id is not None

@pytest.mark.asyncio
async def test_get_all_products(setup_database, test_session: AsyncSession):
    """
    Hybrid unit/integration test for the get_all_products service function.
    - Creates a single product and retrieves all products.
    - Verifies exactly one product is returned with the correct title.
    """
    product_data = ProductBase(title="Test Product")
    await create_product(test_session, product_data)
    products = await get_all_products(test_session)
    assert len(products) == 1
    assert products[0].title == "Test Product"

@pytest.mark.asyncio
async def test_get_product(setup_database, test_session: AsyncSession):
    """
    Hybrid unit/integration test for the get_product service function.
    - Creates a product and retrieves it by ID.
    - Verifies the fetched product's title and ID match the created product.
    """
    product_data = ProductBase(title="Test Product")
    product = await create_product(test_session, product_data)
    fetched_product = await get_product(product.id, test_session)
    assert fetched_product.title == "Test Product"
    assert fetched_product.id == product.id

@pytest.mark.asyncio
async def test_get_product_not_found(setup_database, test_session: AsyncSession):
    """
    Hybrid unit/integration test for get_product with a nonexistent product.
    - Attempts to retrieve a product with ID 999, which doesn't exist.
    - Verifies a 404 HTTPException is raised with the correct message.
    """
    with pytest.raises(HTTPException) as exc:
        await get_product(999, test_session)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Product not found"

@pytest.mark.asyncio
async def test_update_product(setup_database, test_session: AsyncSession):
    """
    Hybrid unit/integration test for the update_product service function.
    - Creates a product, updates its title to "Updated Product".
    - Verifies the updated product has the new title and same ID.
    """
    product_data = ProductBase(title="Test Product")
    product = await create_product(test_session, product_data)
    update_data = ProductUpdate(title="Updated Product")
    updated_product = await update_product(product.id, update_data, test_session)
    assert updated_product.title == "Updated Product"
    assert updated_product.id == product.id

@pytest.mark.asyncio
async def test_update_product_not_found(setup_database, test_session: AsyncSession):
    """
    Hybrid unit/integration test for update_product with a nonexistent product.
    - Attempts to update a product with ID 999, which doesn't exist.
    - Verifies a 404 HTTPException is raised with the correct message.
    """
    update_data = ProductUpdate(title="Updated Product")
    with pytest.raises(HTTPException) as exc:
        await update_product(999, update_data, test_session)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Product not found"

@pytest.mark.asyncio
async def test_delete_product(setup_database, test_session: AsyncSession):
    """
    Hybrid unit/integration test for the delete_product service function.
    - Creates a product, deletes it, and verifies the success message.
    - Attempts to retrieve the deleted product and verifies a 404 HTTPException.
    """
    product_data = ProductBase(title="Test Product")
    product = await create_product(test_session, product_data)
    result = await delete_product(product.id, test_session)
    assert result == {"detail": "Product deleted successfully"}
    with pytest.raises(HTTPException) as exc:
        await get_product(product.id, test_session)
    assert exc.value.status_code == 404











