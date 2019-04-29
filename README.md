# Predicting_Poverty_based_on_Satellite_Images

1) We pulled the satellite Images from the Google Map API using coordinates extracted from the health survey data API (https://api.dhsprogram.com/#/index.html).
2) We downloaded two different files from the health survey data (https://dhsprogram.com/data/dataset_admin/index.cfm) 
  - the survey data of india which contains the region information
  - the wealth index data which contains the wealth index of the regions
3) after that we map regions from the survey data with welath index data to find out the welath index bucket(lower, middle) .
   we did not considered after level classes due to inbalancing in the data.
4) after that we map Images to different poverty bucket using above data to label Images for classification purpose.
5) we used pretrained model inception net to trained our Images.
6) we achived 71 % validation accuracy.
