/* Copyright 2015, 2019 Google Inc. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
*/

const OFFLINE_VERSION = 1;
const CACHE_NAME = 'offline';

// Replace with the base URL of your GitHub Pages site:
const BASE_URL = 'https://juliusthejules.github.io/localhostack';

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.add(new Request(BASE_URL + '/index.html', { cache: 'reload' }));
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    if ('navigationPreload' in self.registration) {
      await self.registration.navigationPreload.enable();
    }
  })());
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const preloadResponse = await event.preloadResponse;
        if (preloadResponse) {
          return preloadResponse;
        }

        // Only fetch requests for the GitHub Pages site
        if (event.request.url.startsWith(BASE_URL)) {
          const networkResponse = await fetch(event.request);
          return networkResponse;
        }
      } catch (error) {
        console.log('Fetch failed; returning offline page instead.', error);
        const cache = await caches.open(CACHE_NAME);
        const cachedResponse = await cache.match(BASE_URL + '/index.html');
        return cachedResponse;
      }
    })());
  }
});
