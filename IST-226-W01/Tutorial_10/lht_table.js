"use strict";

/*
   New Perspectives on HTML5 and CSS3, 7th Edition
   Tutorial 10
   Review Assignment

   Author: Louis Fennell III
   Date:   11/13/22

	
*/

/* Sets the date displayed in the calendar */
var thisDay = new Date("August 30, 2018");

/* Write the HTML code for the event list table */
var tableHTML = "<table id='eventTable'>" +
                  "<caption>Upcoming Events</caption>" +
                  "<tr><th>Date</th><th>Event</th><th>Price</th></tr>";

/* Sets the endDate for the event list 14 days from the set date (thisDay) */
var endDate = new Date(thisDay.getTime() + 14 * 24 * 60 * 60 * 1000);

/* For loop through the eventDates array */
for (var i = 0; i < eventDates.length; i++) {
      var eventDate = new Date(eventDates[i]);
      var eventDay = eventDate.toDateString();
      var eventTime = eventDate.toLocaleTimeString();

   /* If the event is within the two week window, displays it on the page */
   if (thisDay <= eventDate && eventDate <= endDate) {
      tableHTML += "<tr>";
      tableHTML += "<td>" + eventDay + " @ " + eventTime + "</td>";
      tableHTML += "<td>" + eventDescriptions[i] + "</td>";
      tableHTML += "<td>" + eventPrices[i] + "</td>";
      tableHTML += "</tr>"
   }
}
   tableHTML += "</table>";

/* Writes the HTML code to the eventList */
document.getElementById("eventList").innerHTML = tableHTML;