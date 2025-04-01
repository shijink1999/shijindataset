{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Lab | Data Structures "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise: Managing Customer Orders\n",
    "\n",
    "As part of a business venture, you are starting an online store that sells various products. To ensure smooth operations, you need to develop a program that manages customer orders and inventory.\n",
    "\n",
    "Follow the steps below to complete the exercise:\n",
    "\n",
    "1. Define a list called `products` that contains the following items: \"t-shirt\", \"mug\", \"hat\", \"book\", \"keychain\".\n",
    "\n",
    "2. Create an empty dictionary called `inventory`.\n",
    "\n",
    "3. Ask the user to input the quantity of each product available in the inventory. Use the product names from the `products` list as keys in the `inventory` dictionary and assign the respective quantities as values.\n",
    "\n",
    "4. Create an empty set called `customer_orders`.\n",
    "\n",
    "5. Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of \"t-shirt\", \"mug\", \"hat\", \"book\" or \"keychain\". Add each product name to the `customer_orders` set.\n",
    "\n",
    "6. Print the products in the `customer_orders` set.\n",
    "\n",
    "7. Calculate the following order statistics:\n",
    "   - Total Products Ordered: The total number of products in the `customer_orders` set.\n",
    "   - Percentage of Products Ordered: The percentage of products ordered compared to the total available products.\n",
    "   \n",
    "   Store these statistics in a tuple called `order_status`.\n",
    "\n",
    "8. Print the order statistics using the following format:\n",
    "   ```\n",
    "   Order Statistics:\n",
    "   Total Products Ordered: <total_products_ordered>\n",
    "   Percentage of Products Ordered: <percentage_ordered>% \n",
    "   ```\n",
    "\n",
    "9. Update the inventory by subtracting 1 from the quantity of each product. Modify the `inventory` dictionary accordingly.\n",
    "\n",
    "10. Print the updated inventory, displaying the quantity of each product on separate lines.\n",
    "\n",
    "Solve the exercise by implementing the steps using the Python concepts of lists, dictionaries, sets, and basic input/output operations. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1\n",
    "products = [ \"t-shirt\", \"mug\", \"hat\", \"book\", \"keychain\" ]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory = {}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " Enter quantity for t-shirt:  10\n",
      " Enter quantity for mug:  6\n",
      " Enter quantity for hat:  7\n",
      " Enter quantity for book:  0\n",
      " Enter quantity for keychain:  0\n"
     ]
    }
   ],
   "source": [
    "for product in products :\n",
    "    quantity = int ( input(f\" Enter quantity for {product}: \"))\n",
    "    inventory[product] = quantity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "customer_orders = set()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Please enter 3 products you want to order (choose from t-shirt, mug,hat, book,keychain): \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter product name :  t-shirt \n",
      "Enter product name :  mug\n",
      "Enter product name :  hat\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n Please enter 3 products you want to order (choose from t-shirt, mug,hat, book,keychain): \")\n",
    "for i in range (3):\n",
    "    order = input(\"Enter product name : \").strip().lower()\n",
    "    if order in products :\n",
    "        customer_orders .add(order)\n",
    "    else:\n",
    "        print(\"invalid product.please choose from the given option\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Products ordered:  {'hat', 't-shirt', 'mug'}\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n Products ordered: \", customer_orders)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_products_ordered = len(customer_orders)\n",
    "percentage_ordered = (total_products_ordered/len(products)) * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "order_status =(total_products_ordered, percentage_ordered)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Order Statistics: \n",
      "Total products ordered : 3\n",
      "Percentage of products ordered: 60.00%\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n Order Statistics: \")\n",
    "print(f\"Total products ordered : {order_status[0]}\")\n",
    "print(f\"Percentage of products ordered: {order_status[1]:.2f}%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "for product in customer_orders:\n",
    "    if inventory[product]>0:\n",
    "        inventory[product] -= 1\n",
    "    else:\n",
    "        print(f\"Warning : {product} is out of stock!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Updated Inventory: \n",
      "t-shirt: 9\n",
      "mug: 5\n",
      "hat: 6\n",
      "book: 0\n",
      "keychain: 0\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n Updated Inventory: \")\n",
    "for product, quantity in inventory.items():\n",
    "    print(f\"{product}: {quantity}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
