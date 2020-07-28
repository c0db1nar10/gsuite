#RG-Cual es el objetivo? Actualizar los atrasados? Cuales son las 5 que habla en el correo? Cada cuando se corre este proceso?
@frappe.whitelist()
def atrasado():
    return frappe.db.sql("UPDATE `sura.totall.mx`.`tabSales Invoice` a left join `sura.totall.mx`.`tabCustomer` b on a.customer = b.customer_name set b.atrasado = DATEDIFF(CURDATE(), a.posting_date), b.factura = a.name where a.status = 'Overdue' or a.status = 'Unpaid'")


@frappe.whitelist()
def bloqueado():
    return frappe.db.sql("UPDATE `sura.totall.mx`.`tabCustomer` set congelado = 1, credit_limit = 1 where atrasado >= 40 and clave like '%%CC%%'")

@frappe.whitelist()
def desbloqueado():
    return frappe.db.sql("UPDATE `sura.totall.mx`.`tabCustomer` 
                         congelado = 0, credit_limit = 0 where atrasado < 40 and clave like '%%CC%%'")

@frappe.whitelist()
def sinatraso():
    return frappe.db.sql("UPDATE `sura.totall.mx`.`tabSales Invoice` a left join `sura.totall.mx`.`tabCustomer` b on a.customer = b.customer_name set b.atrasado = 0 where a.customer not in (Select customer from `sura.totall.mx`.`tabSales Invoice` where status = 'overdue' or status = 'unpaid')")
