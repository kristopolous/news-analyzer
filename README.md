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


## Rationale

The two dominant media classification vectors of truthfulness and political bias are both coarse and inaccurately  decreed from a single opinion or crowdsourced.

Even a two-dimensional [political compass](https://en.wikipedia.org/wiki/Political_compass) model is insufficient because it relies on stances to be bucketed into that system and correlated with other stances in the bucket.

A more accurate model would depict an enumeration of perspectives on a specific event or idea and a commitment level to such a perspective. 

This approach permits for both predictive entanglement and disintanglement.

### Example 1

For simplicity purposes, we'll binary classify (for/against) a number of issues, deal with their permutation and then show how the dominant models fail and the more direct ones succeed.

The issues will be gun rights, immigration, and antiterrorism.  An enumeration of each position is as follows:

  * guns: "for" means acquisition, storage, and use of firearms should have fewer restrictions. "against" is the opposite.
  * immigration: "for" means paths to citizenship should be expediated and quotas such as lottery system should be eliminated. "against" is the opposite.
  * antiterrorism: "for" means granting power to the state to surveille and detain without oversight. "against" means the state shouldn't have such privileges.

We'll try to bucket all enumerations using a number of political labels, the label 'X' will mean the "for" category.

  
guns  immigration antiterrorism 
      
    x 
  x   liberal
  x x libertarian
x     
x   x conservative
x x   anarchism
x x x ??

