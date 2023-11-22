self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('localhostack-cache')
      .then(cache => {
        return cache.addAll([
          '/',
          'script.js',
          'server.py'
        ]);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
