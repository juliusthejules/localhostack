/*
  Copyright 2015, 2019 Google Inc. All Rights Reserved.
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

const CACHE_NAME = 'offline';
const RESOURCES_TO_CACHE = [
  './',
  './index.html',
  './script.js',
  './sw.js',
  './app.webmanifest',
  './social.png',
  './favicon.ico',
  './icon-192x192.png',
  './icon-256x256.png',
  './icon-384x384.png',
  './icon-512x512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(RESOURCES_TO_CACHE);
  })());
});

self.addEventListener('fetch', (event) => {
  event.respondWith((async () => {
    try {
      const response = await fetch(event.request);
      return response;
    } catch (error) {
      const cachedResponse = await caches.match(event.request);
      return cachedResponse || response; // If not in cache try network again
    }
  })());
});
