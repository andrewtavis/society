<a id="top"></a>

<div align="center">
  <a href="https://codeberg.org/andrewtavis/society"><img src="https://codeberg.org/andrewtavis/society/raw/branch/main/resources/society_logo_transparent.png" width="498" height="126"></a>
</div>

<ol></ol>

[![license](https://img.shields.io/github/license/andrewtavis/society)](https://codeberg.org/andrewtavis/society/src/branch/main/LICENSE.txt)
[![coc](https://img.shields.io/badge/coc-Contributor%20Covenant-ff69b4.svg)](https://codeberg.org/andrewtavis/society/src/branch/main/.forgejo/CODE_OF_CONDUCT.md)
[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### A board game that mixes Settlers of Catan and Monopoly

# Contents

- [Maintenance](#maintenance)
- [Description](#description)
- [Board](#board)
- [Play](#play)
- [Winning](#winning)
- [Components](#components)
- [Cards](#cards)
- [Resources](#resources)
- [The Market](#the-market)
- [To-Do](#to-do)

# Maintenance

`Society` is maintained at [codeberg.org/andrewtavis/society](https://codeberg.org/andrewtavis/society). Please visit this remote repository for issues and pull requests.

# Description

**Society** is a version of Monopoly that adds elements of Settlers of Catan for social interaction and teamwork. Discussions of how it could work can take place in the [Issues](https://codeberg.org/andrewtavis/society/issues). [components/society_designs.sketch](https://codeberg.org/andrewtavis/society/src/branch/main/components/society_designs.sketch) is a full [Sketch](https://www.sketch.com/) file that has baseline designs for the board, cards, bills, and other game elements. [components/cards](https://codeberg.org/andrewtavis/society/src/branch/main/components/cards/) further has text files that describe potential action and event cards as well as [Inkscape](https://inkscape.org/) and [Python script](https://codeberg.org/andrewtavis/society/src/branch/main/scripts/) generated versions of the cards.

<sub><a href="#top">Back to top.</a></sub>

# Board

<br />

<div align="center">
  <img src="https://codeberg.org/andrewtavis/society/raw/branch/main/components/png/society_board.png" width="650" height="650">
</div>

<br />

The Society board is split up based on cardinal directions oriented around the game logo. This allows events in the game to effect specific areas of the board. For physical resources, the playing field is split so that materials and products are produced in the south (black), and energy and technology are produced in the north (white). For institutions, there is a campus in the west (dark grey) and east (light grey) corners that each have a university and a hospital, with the north and south of the board being districts that each have their own precinct and court at the respective corners.

Along the edge of the inner board are numbers that indicate the current turn. This allows players to choose a turn limit before play, that events should happen at a given turn, provide players with an action card at a given turn, etc.

<sub><a href="#top">Back to top.</a></sub>

# Play

A fundamental decision at the start of Society was that everything can be owned privately or publicly. Think of this in terms of playing Monopoly, but one of the players could own the jail. The full details of how private and public ownership of companies and institutions have yet to be decided on, but the current idea is that in private ownership a player pays another for resources, and in public ownership the costs would go to the middle of the board. These communal funds and resources could then be used to upgrade public companies and institutions. Public ownership would be triggered by a player not wanting to buy something that they had landed on, with communal funds then being used to buy it if a majority of players agree to purchase it publicly. In this way there can be both public and private companies and most importantly institutions, thus simulating all baseline aspects of an economy.

Play is similar to that of Monopoly where players role, go to the directed space, can buy it if it's unavailable, and if it's owned would then interact with the owner. Society adds resources to the game that function in a similar manner to those in Settlers of Catan. Rather than simply paying the owner and getting nothing in return as in Monopoly, Society gives a player the option to buy resources from the owner. Prices for the resources would be based on the current market price for a given resource, thus adding a macroeconomic element to the game. A player can always choose to deal with the market on their turn - potentially with a transfer cost that would be determined by the market - but in dealing with the local economy the communal resources of all players increases, which thus allows for the society to be developed more easily.

As in Monopoly, companies and institutions can be upgraded, which then allows them to produce more of their given resource as in Settlers of Catan. Also as in Settlers, upgrades are done via a specific combination of resources rather than with money. Uniquely to Society though is the concept of share holding in a company. Rather than needing to buy the whole company to upgrade it, players can own shares of a company with others. Each part of the company would need to be upgraded before the next level of upgrade would be allowed. The spaces for the company on the board thus represent 50% or 33% shares, with the player than marking the space as belonging to them using the triangle above the space.

Players can also choose the difficulty of the game at the start. This would entail not including some of the institutional resources (health, force, transfer costs, taxes, etc), which would further remove certain cards from the game.

There are many aspects of play that are yet to be decided on. Feel free to check the [Issues](https://codeberg.org/andrewtavis/society/issues) or make one of your own to discuss further.

<sub><a href="#top">Back to top.</a></sub>

# Winning

There are many ways to win in Society. The baseline condition to victory would be having the most resources at the end of the game's turn limit, with this including the resources used to upgrade ones companies and institutions. If playing with health, if all other players have died then the survivor would also be the winner. There is the potential to also add victory conditions such as goals that a player needs to achieve in order to win.

<sub><a href="#top">Back to top.</a></sub>

# Components

<br />

<div align="center">
  <img src="https://codeberg.org/andrewtavis/society/raw/branch/main/components/png/company_institution_cards.png" width="817" height="1158">
</div>

<br />

Components for Society would be a pair of dice, player tokens, bills, tokens that represent resources, cards that describe events in the game or actions that players can take, a market board that describes the current prices of certain resources, cards that show ownership and upgrade steps for companies and institutions, tokens to mark the upgrade level of a company or institution, and markers to show ownership of companies or institutions.

<sub><a href="#top">Back to top.</a></sub>

# Cards

<br />

<div align="center">
  <img src="https://codeberg.org/andrewtavis/society/raw/branch/main/components/png/event_action_cards.png" width="750" height="250">
</div>

<br />

### Events

Event cards are represented by the `?` symbol. They are played instantly, with players needing to then react to the description on the card.

### Actions

Action cards are represented by the `!` symbol. These cards are held in a player's hand and played throughout the game. Certain cards could necessarily be played during a player's turn, while others could be played at other times to disrupt the turns of others.

<sub><a href="#top">Back to top.</a></sub>

# Resources

<br />

<div align="center">
  <img src="https://codeberg.org/andrewtavis/society/raw/branch/main/components/png/resource_tokens.png" width="826" height="476">
</div>

<br />

### Physical

The physical resources are materials, products, energy and technology. Each is needed to upgrade companies or institutions based on what is produced and what level is being upgraded to. Physical resources could also be required in responses to event cards.

### Institutional

The institutional resources are knowledge, influence, health and force. Each of these is used in varying ways throughout play, with knowledge and influence being predominantly used to develop companies or institutions, health being needed to stay alive or out of a hospital, and force being used to defend companies, institutions, or player tokens.

<sub><a href="#top">Back to top.</a></sub>

# The Market

<br />

<div align="center">
  <img src="https://codeberg.org/andrewtavis/society/raw/branch/main/components/png/the_market.png" width="750" height="619">
</div>

<br />

The most complicated part of Society is the market, which in turn adds one of the more interesting and educational elements to the game. The Market determines the prices for certain resources, with prices being effected by events in the game. All physical resources are necessary for play, as well as knowledge and influence that are required to upgrade companies and institutions. All other aspects of the game are optional.

<sub><a href="#top">Back to top.</a></sub>

# To-Do

Work that is in progress or could be implemented is tracked in the [Issues](https://codeberg.org/andrewtavis/society/issues). Please see the [contribution guidelines](https://codeberg.org/andrewtavis/society/src/branch/main/CONTRIBUTING.md) if you are interested in contributing to Society.

<sub><a href="#top">Back to top.</a></sub>
