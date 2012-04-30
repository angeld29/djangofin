delete from finances_ticket;
delete from finances_good;
delete from finances_article;
delete from finances_income;

insert into finances_article (id , label)
select id, label from poluchk.voc_articles
where fake = 0;
insert into finances_good (id , label, article_id)
select id, label, id_voc_article from poluchk.voc_goods
where fake = 0;
insert into finances_ticket ( id, user_id , dt, total, good_id, comment )
select 
	id,
	case 
	 when id_user = 3 then 3 
	 when id_user = 4 then 2
	 ELSE 1
	END as  user_id,
	dt, total, id_voc_goods, comment
	from poluchk.tickets
where fake = 0;
insert into finances_income ( id , user_id, amount, dt)
select 
	id,
	case 
	 when id_user = 3 then 3 
	 when id_user = 4 then 2
	 ELSE 1
	END as  user_id,
	amount, dt
from poluchk.income
where fake = 0;
