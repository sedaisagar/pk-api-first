// Comment

// Fetch Api To Get Products
// Append items to the DOM


document.addEventListener("DOMContentLoaded", function() {
    fetch("http://127.0.0.1:8001/api/products/", {method: "GET"})
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const productList = document.getElementById("productContainer");
            
            data.forEach(product => {
                const productItem = document.createElement("div");
                productItem.className = "col-md-4 mb-4";
                productItem.innerHTML = `
                    <div class="card h-100">
                        <img src="${product.image}" class="card-img-top" style="height:200px;" alt="${product.title}">
                        <div class="card-body">
                            <h5 class="card-title">${product.title}</h5>
                            <p class="card-text">${product.description}</p>
                            <p class="card-text"><strong>Price:</strong> $${product.price}</p>
                                <form action="https://rc-epay.esewa.com.np/api/epay/main/v2/form" method="POST">
                                
                                    <input type="hidden" id="amount" name="amount" value="${product?.price?.toFixed(2)}" required>
                                    <input type="hidden" id="tax_amount" name="tax_amount" value ="0" required>
                                    <input type="hidden" id="total_amount" name="total_amount" value="${product?.price?.toFixed(2)}" required>
                                    <input type="hidden" id="transaction_uuid" name="transaction_uuid" value="${product.transaction_uuid}" required>
                                    <input type="hidden" id="product_code" name="product_code" value ="EPAYTEST" required>
                                    <input type="hidden" id="product_service_charge" name="product_service_charge" value="0" required>
                                    <input type="hidden" id="product_delivery_charge" name="product_delivery_charge" value="0" required>
                                    <input type="hidden" id="success_url" name="success_url" value="https://developer.esewa.com.np/success" required>
                                    <input type="hidden" id="failure_url" name="failure_url" value="https://developer.esewa.com.np/failure" required>
                                    <input type="hidden" id="signed_field_names" name="signed_field_names" value="total_amount,transaction_uuid,product_code" required>
                                    <input type="hidden" id="signature" name="signature" value="${product.signature}" required>
                                    <button type="submit" class="btn btn-success">Pay with esewa</button>
                                </form>
                                    
                        </div>
                    </div>
               ` ;
                productList.appendChild(productItem);
            });
         });
});