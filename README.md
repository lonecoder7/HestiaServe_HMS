# Restaurant Management System

## Overview
The **Restaurant Management System** is a Python-based application designed to help restaurant owners and managers efficiently manage their menu, track customer orders, and generate reports. The system uses a **MySQL** database to store customer and billing information and provides an intuitive interface for both administrators and customers.

## Features

### **Admin Panel**
- Add, modify, and delete menu items.
- Generate reports on total sales, bills, and revenue.
- Manage customer details and track orders.
- View tax details and daily sales.

### **Customer Panel**
- Register as a new customer and log in.
- Browse the menu and place orders.
- Generate bills for purchases.

## Technologies Used
- **Python** (Core application logic)
- **MySQL** (Database for storing customer and order details)
- **Pickle** (File handling for menu data)
- **Matplotlib** (Graphical reports and visualizations)
- **Tabulate** (Formatted table output)

## Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/lonecoder7/restaurant-management-system.git
cd restaurant-management-system
```

### **2. Install Required Packages**
Ensure you have Python installed, then run the following command to install dependencies:
```bash
pip install mysql-connector-python matplotlib tabulate
```

### **3. Set Up the MySQL Database**
1. Start your MySQL server.
2. Create a new database named **`restra`**:
```sql
CREATE DATABASE restra;
USE restra;
```
3. Create the required tables:
```sql
CREATE TABLE bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10,2),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15) UNIQUE
);

CREATE TABLE coss (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_details TEXT,
    total_amount DECIMAL(10,2)
);

CREATE TABLE tr (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_details TEXT
);

CREATE TABLE tax (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tax_rate DECIMAL(5,2)
);
```
4. Update the **MySQL connection settings** in `restaurant_management_system.py` with your credentials:
```python
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="restra"
)
```

### **4. Run the Application**
```bash
python restaurant_management_system.py
```

## Usage

### **Admin Login**
- **CEO Password:** `112233`
- **Manager Password:** `102030`

### **Customer Login**
- Register as a new customer or log in using your **customer ID** or **phone number**.

### **Order Processing**
1. View available menu items.
2. Select items and place an order.
3. Generate a bill after placing an order.

## Notes
- Ensure that the **MySQL server** is running before starting the application.
- The application uses a **restra.dat** file to store menu items. Keep this file in the same directory as the script.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a pull request.

## License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Thanks to all contributors and the open-source community for their support!

