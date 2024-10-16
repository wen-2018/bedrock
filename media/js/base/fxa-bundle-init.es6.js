/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

import FxaLink from './fxa-link.es6.js';
import FxaAttribution from './fxa-attribution.es6.js';
import FxaCoupon from './fxa-coupon.es6.js';

// Pass coupon URL query parameters through to Mozilla account subscription links.
FxaCoupon.init(window.location.href);

if (typeof window._SearchParams !== 'undefined') {
    const urlParams = new window._SearchParams();

    // Track external URL parameter referrals for Mozilla account links.
    FxaAttribution.init(urlParams.params);

    // Configure Mozilla account links for Sync on desktop.
    FxaLink.init();
}
