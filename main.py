from pyscript import display, document

def create_order(e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    prod6 = document.getElementById("item6")
    prod7 = document.getElementById("item7")
    prod8 = document.getElementById("item8")
    prod9 = document.getElementById("item9")

    subtotal = (
        float(prod1.value) * prod1.checked +
        float(prod2.value) * prod2.checked +
        float(prod3.value) * prod3.checked +
        float(prod4.value) * prod4.checked +
        float(prod5.value) * prod5.checked +
        float(prod6.value) * prod6.checked +
        float(prod7.value) * prod7.checked +
        float(prod8.value) * prod8.checked +
        float(prod9.value) * prod9.checked
    )

    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt = f"""
    <h3>==== Receipt ====</h3>
    <p>Subtotal: <img src="Miscpon.webp" width="20"> {subtotal:.2f}</p>
    <p>Tax: <img src="Miscpon.webp" width="20"> {tax:.2f}</p>
    <p><strong>Total: <img src="Miscpon.webp" width="20"> {total:.2f}</strong></p>
    """

    document.getElementById("show").innerHTML = receipt

def SKU_generator(e):

    category = ""

    if document.getElementById("badges").checked:
        category = "Badges"

    elif document.getElementById("hats").checked:
        category = "Hats"

    elif document.getElementById("cosmetics").checked:
        category = "Cosmetics"


    product_name = document.getElementById("product_name")

    quantity = document.getElementById("quantity")


    product = product_name.value
    stock = quantity.value


    sku = category[:3].upper() + "-" + product[:4].upper() + "-" + stock

    document.getElementById("sku_output").innerHTML = ""

    display("SKU: " + sku, target="sku_output")