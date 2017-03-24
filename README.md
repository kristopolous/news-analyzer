## Overview

An attempt to quantify bias and framing in the media.

Bias here means a consistent adherence to a perspective. Having more bias is demonstrated through more adherence and a less negotiated stance.

Framing here means intentionally representing an event or idea. There are a number of quantifiable forms of framing:

  * size: Amount of screen-real estate used along with its duration.
  * place: Location and frequency of placement of detail or fact within the body of a work.
  * word: The sentiments of adjectives and verbs used.
  * context: The density of references to prior events.
  * amplitude: Location and number of clicks to get to the content.

The theory is being able to reliably quantify these things can lead to a predictive model of media coverage based on analysis of an existing corpus.

The magnitude of a news event is the computed deviation of its coverage from the predicted model.


The long term intentions here are to be able to automate and historically map the chronicling of a news story

Optimistically, the goals are to be able to identify fractures in coverage and the introduction of bias, spin, and frame.

## Rationale

The two dominant media classification vectors of truthfulness and political bias are both coarse and inaccurately  decreed from a single opinion or crowdsourced.

Even a two-dimensional [political compass](https://en.wikipedia.org/wiki/Political_compass) model is insufficient because it relies on stances to be bucketed into that system and correlated with other stances in the bucket.

A more accurate model would depict an enumeration of perspectives on a specific event or idea and a commitment level to such a perspective. 

This approach permits for both predictive entanglement and disintanglement.

## notes

checksum for unique entries

important columns:

  * source
  * checksum
  * date
  * payload

## HTML scraping
Mobile vs. Desktop
render in phantomjs

Record:

  * top/left
  * height/width
  * content

### Information loss
It may be better to hold on to the HTML for now to avoid potential
information loss:

  * text size, color, and weight
  * image dimensions

concerns over file-system limits
have an articles db

  meta information can change

  In one test, taking out all the non-article related stuff reduced the file-size by 93%. This isn't only a matter of saving space, but it's also a matter of cutting out noise
