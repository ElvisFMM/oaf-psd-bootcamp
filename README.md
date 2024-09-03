# S&P 500 Tracker

![alt text](https://github.com/ElvisFMM/oaf-psd-bootcamp/blob/branch1/pictures/stocks.JPG)
*Better to buy in when the board is red - think of it as a discount*

This is a summary of my project for the Pofessional Software Bootcamp through Open Avenues.  The project is still a work in progress - I'll be updating it more next month.


## Table of Contents 
* [Motivation](#motivation)
* [Summary of approach](#summary-of-approach)
* [Results](#results)
* [My approach in more detail](#my-approach-in-more-detail)
	* [Data sources](#data-sources)
	* [Sampling](#sampling)
* [What I learned](#what-i-learned)
* [Future directions](#future-directions)
* [Project Organization](#project-organization)


## Motivation

I have always been intrigued by investing and the power of compound interest. I wanted to create this application to track the status of the S&P 500 index to get updates on its price.


## Summary of approach

### When is a good time to buy-in?

For this project I wanted to have updates for when it is a good time to buy index funds. I decided to have a search feature for different stocks while also a visual for current S&P 500 price status.

*Tech Stack*

* Backend - Python (flask library), Finnhub API (https://finnhub.io/docs/api/library)
* Frontend - HTML, JavaScript
* Database - Sqlite 


## Results & Future Directions

The application presents a login screen which once successfully logged in you can use the stock search function to view live data for any stock on the market. This information is up to date. During further development I wish to track specific index stocks to notify once their is a certain drop in its price. This will then alow to have the best chance to buy stocks for a good price.

## What I learned

I've learned quite alot from the bootcamp such as proper ways to structure code to make it more modular and reusable. This is present when coding Objects with a goal of having inheritance or using depandency injection to facilitate changing certain paraments. I don't have much experience using API's and using them to query live stock information was awesome to see. 

