# whoisAzureFunction

This Azure function is used to automatically detect when a domain name changes its registration status with the Domain Registrar. It can be used to send a notification when a domain name you want is available for purchase.

The 'HTTPService' can be called to query the DNS information for a domain, and the 'Timer' service can be run in Azure Functions to check the status of a domain at a set interval.

For example, set the timer service to query the DNS records for www.google.com each 5 minutes. If www.google.com changes status, send an email to your inbox to notify you of the change.
