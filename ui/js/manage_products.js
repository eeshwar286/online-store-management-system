// Fetch all products from the Flask API and display them
function fetchProducts() {
    fetch('http://localhost:5000/getProducts')
        .then(response => response.json())
        .then(data => {
            const productList = document.getElementById('product-list');
            productList.innerHTML = ''; // Clear the existing list

            // Iterate through the products and add them to the product list
            data.forEach(product => {
                const listItem = document.createElement('li');
                listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
                listItem.innerHTML = `
                    ${product.product_name} - $${product.price_per_unit} (UOM: ${product.uom_name})
                    <button class="btn btn-danger btn-sm" onclick="deleteProduct(${product.product_id})">Remove</button>
                `;
                productList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Add a new product
function addProduct(event) {
    event.preventDefault();

    const productName = document.getElementById('product-name').value;
    const productPrice = document.getElementById('product-price').value;
    const uom = document.getElementById('uom').value;

    const formData = new FormData();
    formData.append('product_name', productName);
    formData.append('price_per_unit', productPrice);
    formData.append('uom_id', uom);

    fetch('http://localhost:5000/addProduct', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Product added successfully:', data);
        fetchProducts(); // Refresh the product list after adding a new product
        document.getElementById('product-form').reset(); // Clear the form inputs
    })
    .catch(error => console.error('Error adding product:', error));
}

// Delete a product
function deleteProduct(productId) {
    const formData = new FormData();
    formData.append('product_id', productId);

    fetch('http://localhost:5000/deleteProduct', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Product deleted successfully:', data);
        fetchProducts(); // Refresh the product list after deletion
    })
    .catch(error => console.error('Error deleting product:', error));
}

// Call fetchProducts() when the page loads to display all products
document.addEventListener('DOMContentLoaded', fetchProducts);
