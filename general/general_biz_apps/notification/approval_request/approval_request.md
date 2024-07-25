<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style>
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header, .footer {
            text-align: center;
        }
        .content p {
            color: black;
            margin: 0 0 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <!-- Header content here if applicable -->
        </div>

        <div class="content">
            <p>Greetings,</p>

            <p>This is to inform you that your request for approval as detailed below has been declined.</p>

            <table>
                <tr>
                    <th>Requisition ID</th>
                    <td>{{ doc.name }}</td>
                </tr>
                <tr>
                    <th>Beneficiary</th>
                    <td>{{ doc.beneficiary }} or {{ doc.supplier_name }}</td>
                </tr>
                <tr>
                    <th>Department</th>
                    <td>{{ doc.requesting_department }}</td>
                </tr>
                <tr>
                    <th>Purpose</th>
                    <td>{{ doc.purpose }}</td>
                </tr>
                <tr>
                    <th>Trans Currency</th>
                    <td>{{ doc.currency }}</td>
                </tr>
                <tr>
                    <th>Amount</th>
                    <td>{{ doc.amount }}</td>
                </tr>
                <tr>
                    <th>Amount In Words</th>
                    <td>{{ doc.amount_in_words }}</td>
                </tr>
            </table>

            <p><b>{{ _("A summary of the requisition details can be found on the ERP system: ") }}</b> {{ frappe.utils.get_link_to_form(doc.doctype, doc.name) }}</p>
            <p>You are kindly requested to see your manager for the next line of action.</p>

            <p>Thank you.</p>
        </div>

        <div class="footer">
            <!-- Footer content here if applicable -->
        </div>
    </div>
</body>
</html>
