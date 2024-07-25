<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-color: #e0f7fa;
        }
        .header, .footer {
            text-align: center;
        }
        .content p {
            color: #004d40;
            margin: 0 0 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: #ffffff;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #b2dfdb;
            color: #004d40;
        }
        td {
            color: #00796b;
        }
        .highlight {
            color: #004d40;
            font-weight: bold;
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

            <p>This is to notify you that a Payment Voucher has been created <span class="highlight">{{ doc.name }}</span> for referenced Request document <span class="highlight">{{ doc.approval_doc }}</span> by <span class="highlight">{{ doc.owner }}</span> on <span class="highlight">{{ doc.date }}</span>.</p>

            <table>
                <tr>
                    <th>Requisition ID</th>
                    <td>{{ doc.name }}</td>
                </tr>
                <tr>
                    <th>Beneficiary</th>
                    <td>{{ doc.payee_name }}</td>
                </tr>
                <tr>
                    <th>Department</th>
                    <td>{{ doc.department }}, {{ doc.cost_center }}</td>
                </tr>
                <tr>
                    <th>Purpose</th>
                    <td>{{ doc.transaction_purposes }}</td>
                </tr>
                <tr>
                    <th>Trans Currency</th>
                    <td>{{ doc.payment_currency if doc.payment_currency == "NGN" else doc.amount_paid_in_fc }}</td>
                </tr>
                <tr>
                    <th>Exch Rate</th>
                    <td>{{ doc.exchange_rate if doc.payment_currency != "NGN" else 1 }}</td>
                </tr>
                <tr>
                    <th>Trans Ref</th>
                    <td>{{ doc.reference_no }}</td>
                </tr>
                <tr>
                    <th>Amount</th>
                    <td>{{ doc.amount_paid }} {{ doc.amount_paid_in_fc }}</td>
                </tr>
                <tr>
                    <th>Amount In Words</th>
                    <td>{{ doc.amount_in_words }}</td>
                </tr>
            </table>
            <p><b>{{ _("A summary of the requisition details can be found on the ERP system: ") }}</b> {{ frappe.utils.get_link_to_form(doc.doctype, doc.name) }}</p>

            <p>Kindly process immediately.</p>

            <p>Thank you.</p>
        </div>

        <div class="footer">
            <!-- Footer content here if applicable -->
        </div>
    </div>
</body>
</html>
