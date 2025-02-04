

import pyodbc
import frappe

def fetch_and_create_waybills():
    # Step 1: SQL Server connection setup
    frappe.log_error('test1',"Test1 successful")
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-2VPR9IB\\BCDEMO;"
        "Database=agility;"
        "Trusted_Connection=yes;"
    )

    try:
        # Connect to SQL Server
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Step 2: Fetch specific columns from the agility table
        query = """
            SELECT 
                Date_Created,
                Payment_Status,
                Shipment_ID,
                Agility_Customer_Code,
                Customer_ID,
                Customer_Name,
                Company,
                Item_Description,
                Customer_Type,
                Departure_Service_Centre_ID,
                Product_Type,
                Business_Class,
                Business_Type,
                Waybill_No,
                Destination_Service_Centre_ID,
                Currency,
                Exch_Rate,
                Weight,
                Grand_Total,
                VAT_Excl_Rate,
                Real_Weighted_Price,
                VAT,
                Total
            FROM shipment;
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        # Step 3: Column mapping between SQL agility table and Waybill fields
        column_mapping = {
            "date_created": "Date_Created",
            "payment_status": "Payment_Status",
            "shipment_id": "Shipment_ID",
            "agility_customer_code": "Agility_Customer_Code",
            "customer_id": "Customer_ID",
            "customer_name": "Customer_Name",
            "company": "Company",
            "item_description": "Item_Description",
            "customer_type": "Customer_Type",
            "departure_service_centre_id": "Departure_Service_Centre_ID",
            "product_type": "Product_Type",
            "business_class": "Business_Class",
            "business_type": "Business_Type",
            "waybill_no": "Waybill_No",
            "service_center": "Destination_Service_Centre_ID",
            "currency": "Currency",
            "exch_rate": "Exch_Rate",
            "approximate_items_weight": "Weight",
            "grand_total": "Grand_Total",
            "rate": "VAT_Excl_Rate",
            "real_weighted_price": "Real_Weighted_Price",
            "vat": "VAT",
            "total": "Total"
        }

        # Step 4: Loop through rows and create Waybill documents
        for row in rows:
            # Map SQL data to Waybill fields
            waybill_data = {
                field: row[column_index] if column_index < len(row) else None
                for field, column_name in column_mapping.items()
                for column_index, column_description in enumerate(cursor.description)
                if column_name == column_description[0]
            }

            # Create Waybill document in ERPNext
            waybill = frappe.get_doc({
                "doctype": "Waybill",
                **waybill_data  # Unpack mapped fields
            })

            waybill.insert()  # Save the document
            frappe.db.commit()  # Commit the transaction

        print("Waybills created successfully.")
        frappe.log_error('test2',"Test2 successful")

    except pyodbc.Error as ex:
        print(f"An error occurred: {ex}")
    finally:
        if connection:
            connection.close()


# Call the function

