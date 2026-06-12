const fs = require('fs');
let c = fs.readFileSync('C:/Users/WALTON/Downloads/Untitled-1.html', 'utf8');

const replacements = {
  'Ã¢â‚¬â€œ': '–',
  'Ã¢â‚¬â€': '—',
  'Ã‚Â·': '·',
  'Ã¢â€ â€™': '→',
  'Ã°Å¸â€˜¤': '👤',
  'Ã°Å¸â€œ°': '📰',
  'âš½': '⚽',
  'Ã¢Å¡Â½': '⚽',
  'Ã°Å¸â€œâ€¦': '📅',
  'Ã°Å¸â€“¼': '🖼️',
  'Ã°Å¸â€œâ€¹': '📋',
  'Ã°Å¸â€œÂ ': '📁',
  'Ã¢Å¡â„¢Ã¯Â¸Â ': '⚙️',
  'Ã°Å¸â€ Â ': '🔎',
  'Ã°Å¸â€œŠ': '📊',
  'Ã°Å¸â€¦Â°Ã¯Â¸Â ': '🅰️',
  'Ã¢â‚¬Â¦': '…',
  'Ã¢Å“â€¢': '✖',
  'Ã°Å¸Â¤Â ': '🤝',
  'âš¡': '⚡',
  'Ã°Å¸â€œË†': '📈',
  'Ã°Å¸Å½â€°': '🎉',
  'Ã°Å¸â€œ·': '📷',
  'Ã¢â€¢Â ': '═',
  'Ã‚Â©': '©',
  'ðŸŽ®': '🎮',
  'ðŸŽ©': '🎩',
  'ðŸ§¤': '🧤',
  'Ã¢Å¡â„¢': '⚙️',
  'Ã°Å¸Â â€ ': '🏆'
};

for (const [bad, good] of Object.entries(replacements)) {
  c = c.split(bad).join(good);
}

fs.writeFileSync('C:/Users/WALTON/Downloads/Untitled-1.html', c);
console.log("Replaced successfully");
