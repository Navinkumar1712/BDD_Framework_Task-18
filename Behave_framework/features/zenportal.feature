Feature: Zen Portal Login and Logout functionality

    Scenario Outline: Login to Zen Portal with Multiple credentials
        Given the user launches Chrome browser
        When the user open Zen Portal Homepage
        And the user enters username "<username>" and password "<password>"
        And the user click on Sign in button
        Then the user must successfully login and reach the landing page
        And the user must be able to log out of Zen Portal

    Examples:
        | username | password |
        | navinkumar.mk1712@gmail.com | Guvi2025 |
        | kumar@gmail.com | Wrong2024 |

    
# Used a set of valid and invalid credentials for login functionality check on Zen Portal