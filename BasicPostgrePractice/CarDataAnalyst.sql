--Car Data Analyst.
--Which brand sells the most cars?
select brand,Count(*) as MostCars from CarSales group by brand order by MostCars DESC;
--Which city has the most expensive cars?
select city,Count(*) as ExpensiveCars from CarSales group by city order by ExpensiveCars DESC;
--Which years have the highest average prices?
select year,AVG(price) as AveragePrices from CarSales group by year order by AveragePrices DESC;
--Which models appear most frequently?
select model,Count(*) as MostFrequentModel from CarSales group by model order by MostFrequentModel DESC;
