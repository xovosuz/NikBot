import asyncio
import random
import itertools
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
# Manba : @tatu_att
# Creator : @tatu_attt
# ilova : Kim manbani chopsa k"t bob qosin 🤲 (chopmasdan tarqatinglar insof bilan bosin)

BOT_TOKEN = "TOKEN_QOYILADIGAN JOY"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class S(StatesGroup):
    name         = State()
    style_pick   = State()
    combo_pick   = State()
    mix_names    = State()
    custom_name  = State()


_FONT_MAP = {
    "bold": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
    ),
    "italic": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"
    ),
    "bold_italic": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"
    ),
    "fancy": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"
    ),
    "gothic": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"
    ),
    "bubble": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
    ),
    "double": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
    ),
    "small_caps": (
        "abcdefghijklmnopqrstuvwxyz",
        "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    ),
    "wide": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ０１２３４５６７８９"
    ),
    "sans_bold": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    ),
    "mono": (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
    ),
}

def _build_tables():
    tables = {}
    for fname, (src, dst) in _FONT_MAP.items():
        src_chars = list(src)
        dst_chars = list(dst)
        tables[fname] = {s: dst_chars[i] for i, s in enumerate(src_chars) if i < len(dst_chars)}
    return tables

_TABLES = _build_tables()

def font(text: str, fname: str) -> str:
    t = _TABLES.get(fname, {})
    return "".join(t.get(c, c) for c in text)

ALL_FONTS = list(_FONT_MAP.keys())

# 
#                STIL KONFIGURASIYASI
# 
STYLES: dict[str, dict] = {
    "fire": {
        "name": "🔥 Olovli",   "emoji": "🔥",
        "frames":  ["꧁🔥{n}🔥꧂","『🔥{n}🔥』","【🔥{n}🔥】","⟦🔥{n}🔥⟧","▸🔥{n}🔥◂","🌋{n}🌋"],
        "mid":     ["🔥","💥","⚡","🌋","☄️","🔴"],
        "words":   ["Alanga","Olov","Inferno","Blaze","Ember","Flame","PyRo","炎神","Ignis","Vulkan"],
        "adj":     ["Fire","Flame","Blaze","Inferno","Hell","Hot","Burn","Lava"],
    },
    "ice": {
        "name": "❄️ Muzli",    "emoji": "❄️",
        "frames":  ["꧁❄️{n}❄️꧂","「❄️{n}❄️」","〖❄️{n}❄️〗","✦❄️{n}❄️✦","◈❄️{n}❄️◈","🌨️{n}🌨️"],
        "mid":     ["❄️","💎","🔷","🌨️","🧊","🔵"],
        "words":   ["Frost","Glacial","Blizzard","Arctic","Crystal","Cryo","Permafrost","IceLord","SubZero"],
        "adj":     ["Ice","Frost","Snow","Cryo","Freeze","Cold","Winter","Blizzard"],
    },
    "royal": {
        "name": "👑 Qirollik", "emoji": "👑",
        "frames":  ["꧁👑{n}👑꧂","⚜️『{n}』⚜️","♔【{n}】♔","🏆⟦{n}⟧🏆","꧁⚜️{n}⚜️꧂","👑✨{n}✨👑"],
        "mid":     ["👑","⚜️","♔","🏆","💰","🌟","♛"],
        "words":   ["Qirol","Sultan","Emperor","Lord","Rex","Khan","Monarch","Sovereign","Imperator","Kaiser"],
        "adj":     ["King","Royal","Crown","Empire","Regent","Throne","Noble","Supreme"],
    },
    "dark": {
        "name": "💀 Dark",     "emoji": "💀",
        "frames":  ["꧁💀{n}💀꧂","『☠️{n}☠️』","【🖤{n}🖤】","⛓️{n}⛓️","▪💀{n}💀▪","꧁🕷️{n}🕷️꧂"],
        "mid":     ["💀","🖤","⛓️","🕷️","🌑","☠️","🩸"],
        "words":   ["Shadow","Phantom","Void","Abyss","Raven","Venom","Reaper","Necro","Darkness","Oblivion"],
        "adj":     ["Dark","Black","Shadow","Death","Doom","Evil","Grim","Sinister"],
    },
    "electric": {
        "name": "⚡ Elektr",   "emoji": "⚡",
        "frames":  ["꧁⚡{n}⚡꧂","「⚡{n}⚡」","〔⚡{n}⚡〕","◈⚡{n}⚡◈","🌩️{n}🌩️","⚡【{n}】⚡"],
        "mid":     ["⚡","🔋","💡","🌩️","🔌","🟡"],
        "words":   ["Voltage","Thunder","Spark","Neon","Zap","Surge","Gigawatt","Plasma","Pulse","Shock"],
        "adj":     ["Electric","Thunder","Volt","Shock","Zap","Amp","Power","Surge"],
    },
    "flower": {
        "name": "🌸 Nafis",    "emoji": "🌸",
        "frames":  ["🌸•{n}•🌸","✿꒰{n}꒱✿","꒰🌺{n}🌺꒱","🦋•{n}•🦋","🌷『{n}』🌷","✨🌸{n}🌸✨"],
        "mid":     ["🌸","🌺","🌷","🦋","🌼","💐","🌹"],
        "words":   ["Gulsanam","Nilufar","Yasmin","Violetta","Aurora","Luna","Sakura","Blossom","Petal"],
        "adj":     ["Rose","Lily","Bloom","Petal","Flora","Sweet","Angel","Soft"],
    },
    "galaxy": {
        "name": "🌌 Galaktika","emoji": "🌌",
        "frames":  ["꧁🌌{n}🌌꧂","✨『{n}』✨","⭐【{n}】⭐","🪐⟦{n}⟧🪐","🌠✦{n}✦🌠","💫꧁{n}꧂💫"],
        "mid":     ["🌌","✨","⭐","🪐","💫","🌠","🌟"],
        "words":   ["Nebula","Cosmos","Stellar","Astro","Orbit","Nova","Pulsar","Quasar","Andromeda"],
        "adj":     ["Star","Galaxy","Cosmic","Space","Nova","Solar","Lunar","Astral"],
    },
    "ninja": {
        "name": "🥷 Ninja",    "emoji": "🥷",
        "frames":  ["꧁🥷{n}🥷꧂","⚔️『{n}』⚔️","🗡️【{n}】🗡️","忍⟦{n}⟧忍","🎯꧁{n}꧂🎯","⚔️✦{n}✦⚔️"],
        "mid":     ["🥷","⚔️","🗡️","🎯","🌑","忍","🩸"],
        "words":   ["Shinobi","Samurai","Ronin","Kunoichi","Ninjato","Katana","Warrior","Shogun","Sensei"],
        "adj":     ["Ninja","Shadow","Blade","Strike","Stealth","Silent","Swift","Deadly"],
    },
    "cyber": {
        "name": "🤖 Cyber",    "emoji": "🤖",
        "frames":  ["[SYS::{n}::END]","◤Ξ{n}Ξ◥","▓▒░{n}░▒▓","⌬⟨{n}⟩⌬","//:{n}://","∆{n}∆"],
        "mid":     ["🤖","💻","⚙️","🔧","📡","🛸","🔬"],
        "words":   ["Matrix","Nexus","Protocol","Algorithm","Binary","Kernel","Daemon","Root","Byte","Cipher"],
        "adj":     ["Cyber","Bot","AI","Tech","Net","Digital","Virtual","System"],
    },
    "angel": {
        "name": "😇 Angel",    "emoji": "😇",
        "frames":  ["꧁😇{n}😇꧂","✝️『{n}』✝️","🕊️【{n}】🕊️","光꧁{n}꧂光","✨😇{n}😇✨","☁️✨{n}✨☁️"],
        "mid":     ["😇","🕊️","✨","⭐","🌟","☁️","💫"],
        "words":   ["Angel","Seraph","Divine","Sacred","Celestial","Holy","Virtue","Grace","Heaven"],
        "adj":     ["Angel","Divine","Holy","Pure","Light","Bright","Blessed","Sacred"],
    },
    "dragon": {
        "name": "🐉 Ajdaho",   "emoji": "🐉",
        "frames":  ["꧁🐉{n}🐉꧂","🔱『{n}』🔱","龍【{n}】龍","🐲⟦{n}⟧🐲","꧁龍{n}龍꧂","🐉✦{n}✦🐉"],
        "mid":     ["🐉","🔱","龍","🐲","⚔️","🌪️","💥"],
        "words":   ["Dragon","Drake","Wyvern","Draco","Shenron","RyuJin","Typhon","Hydra","Leviathan"],
        "adj":     ["Dragon","Drake","Fire","Scale","Wing","Claw","Fang","Breath"],
    },
    "blood": {
        "name": "🩸 Blood",    "emoji": "🩸",
        "frames":  ["꧁🩸{n}🩸꧂","『🩸{n}🩸』","【🩸{n}🩸】","⟦🩸{n}🩸⟧","▸🩸{n}🩸◂","🩸{n}🩸"],
        "mid":     ["🩸","❤️‍🔥","💔","🫀","♥","🔴"],
        "words":   ["Crimson","Scarlet","Bloody","Gore","Massacre","Slaughter","Carnage","Havoc"],
        "adj":     ["Blood","Red","Crimson","Scarlet","Bloody","Rage","Fury","Wrath"],
    },
    "neon": {
        "name": "🌈 Neon",     "emoji": "🌈",
        "frames":  ["꧁🌈{n}🌈꧂","✦{n}✦","〚{n}〛","꙳{n}꙳","꧁✦{n}✦꧂","【꙳{n}꙳】"],
        "mid":     ["🌈","✦","🎆","🎇","💥","⚡","🌟"],
        "words":   ["Neon","Glow","Vivid","Vibrant","Radiant","Prism","Aurora","Spectrum","Rainbow"],
        "adj":     ["Neon","Glow","Bright","Vivid","Flash","Beam","Shine","Spark"],
    },
}

# 
#            KOMBINATSIYA KONFIGURASIYASI
# 
COMBOS: dict[str, dict] = {
    "fire_ice": {
        "name": "🔥❄️ Olov+Muz",
        "desc": "Olov va muzning uyg'unligi",
        "styles": ["fire", "ice"],
        "special_frames": [
            "꧁🔥{n}❄️꧂", "『🔥{n}❄️』", "【🔥{n}❄️】",
            "⟦🔥{n}❄️⟧", "🌋{n}🧊", "❄️🔥{n}🔥❄️"
        ],
        "special_mid": ["🔥❄️", "❄️🔥", "💎🔥", "🧊💥"],
    },
    "dark_royal": {
        "name": "💀👑 Dark+Qirol",
        "desc": "Qorong'u qirollik",
        "styles": ["dark", "royal"],
        "special_frames": [
            "꧁💀👑{n}👑💀꧂", "『☠️👑{n}👑☠️』",
            "【💀⚜️{n}⚜️💀】", "♛💀{n}💀♛",
            "꧁🖤👑{n}👑🖤꧂", "⛓️👑{n}👑⛓️"
        ],
        "special_mid": ["💀👑", "👑☠️", "🖤⚜️", "⛓️♛"],
    },
    "galaxy_cyber": {
        "name": "🌌🤖 Galaktika+Cyber",
        "desc": "Kosmik texnologiya",
        "styles": ["galaxy", "cyber"],
        "special_frames": [
            "[🌌{n}🌌]", "◤🌟{n}🌟◥", "∆🌌{n}🌌∆",
            "⌬⟨🌠{n}🌠⟩⌬", "//🪐{n}🪐//", "▓🌌{n}🌌▓"
        ],
        "special_mid": ["🌌⚙️", "🤖🌟", "💻🌠", "📡🪐"],
    },
    "ninja_dragon": {
        "name": "🥷🐉 Ninja+Ajdaho",
        "desc": "Ajdaho ninjasi",
        "styles": ["ninja", "dragon"],
        "special_frames": [
            "꧁🥷🐉{n}🐉🥷꧂", "『⚔️龍{n}龍⚔️』",
            "忍🐉{n}🐉忍", "【🥷🔱{n}🔱🥷】",
            "꧁龍⚔️{n}⚔️龍꧂", "🗡️🐲{n}🐲🗡️"
        ],
        "special_mid": ["🥷🐉", "🐉⚔️", "龍忍", "🗡️🔱"],
    },
    "angel_dark": {
        "name": "😇💀 Angel+Dark",
        "desc": "Yorug'lik va qorong'ulik",
        "styles": ["angel", "dark"],
        "special_frames": [
            "꧁😇💀{n}💀😇꧂", "✝️☠️{n}☠️✝️",
            "【🕊️🖤{n}🖤🕊️】", "✨💀{n}💀✨",
            "꧁光🌑{n}🌑光꧂", "☁️⛓️{n}⛓️☁️"
        ],
        "special_mid": ["😇💀", "💀✨", "🖤🕊️", "⛓️☁️"],
    },
    "neon_galaxy": {
        "name": "🌈🌌 Neon+Galaktika",
        "desc": "Neon galaktika",
        "styles": ["neon", "galaxy"],
        "special_frames": [
            "꧁🌈🌌{n}🌌🌈꧂", "✦🌟{n}🌟✦",
            "〚🌈🌠{n}🌠🌈〛", "💥🌌{n}🌌💥",
            "꧁✦🪐{n}🪐✦꧂", "🌈⭐{n}⭐🌈"
        ],
        "special_mid": ["🌈🌌", "✦🎆", "🌟💥", "🌠🌈"],
    },
    "blood_electric": {
        "name": "🩸⚡ Blood+Elektr",
        "desc": "Elektr qon",
        "styles": ["blood", "electric"],
        "special_frames": [
            "꧁🩸⚡{n}⚡🩸꧂", "『🩸⚡{n}⚡🩸』",
            "【💔⚡{n}⚡💔】", "⚡🩸{n}🩸⚡",
            "꧁❤️‍🔥⚡{n}⚡❤️‍🔥꧂", "🌩️🩸{n}🩸🌩️"
        ],
        "special_mid": ["🩸⚡", "⚡💔", "🌩️🩸", "❤️‍🔥⚡"],
    },
    "fire_dragon": {
        "name": "🔥🐉 Olov+Ajdaho",
        "desc": "Olov ajdaho",
        "styles": ["fire", "dragon"],
        "special_frames": [
            "꧁🔥🐉{n}🐉🔥꧂", "『🌋龍{n}龍🌋』",
            "【🔥🔱{n}🔱🔥】", "🐉🔥{n}🔥🐉",
            "꧁龍🔥{n}🔥龍꧂", "🌋🐲{n}🐲🌋"
        ],
        "special_mid": ["🔥🐉", "🐉💥", "龍🌋", "🔱🔥"],
    },
    "royal_galaxy": {
        "name": "👑🌌 Qirol+Galaktika",
        "desc": "Kosmik qirol",
        "styles": ["royal", "galaxy"],
        "special_frames": [
            "꧁👑🌌{n}🌌👑꧂", "⚜️🌟{n}🌟⚜️",
            "♔🌌{n}🌌♔", "【👑🪐{n}🪐👑】",
            "꧁⚜️💫{n}💫⚜️꧂", "🌠♛{n}♛🌠"
        ],
        "special_mid": ["👑🌌", "⚜️🌟", "♔🪐", "💫👑"],
    },
    "cyber_neon": {
        "name": "🤖🌈 Cyber+Neon",
        "desc": "Neon kiberpank",
        "styles": ["cyber", "neon"],
        "special_frames": [
            "[🌈{n}🌈]", "◤✦{n}✦◥",
            "∆🌈{n}🌈∆", "▓✦{n}✦▓",
            "//🌈{n}🌈//", "⌬🌟{n}🌟⌬"
        ],
        "special_mid": ["🤖🌈", "💻✦", "⚙️🎆", "📡🌈"],
    },
}

SEPS = ["_", ".", "•", "·", "×", "ˑ", "꞉", "‿", "ː", "⁞", "᪾"]

def sn(n: int) -> str:
    sub = "₀₁₂₃₄₅₆₇₈₉"
    return "".join(sub[int(d)] for d in str(n) if d.isdigit())


def _pick(lst): return random.choice(lst)

def gen_single(name: str, sk: str) -> list[str]:
    """Bitta stil uchun niklar"""
    s   = STYLES[sk]
    n   = name.strip()
    sep = _pick(SEPS)
    num = random.randint(100, 9999)
    w   = _pick(s["words"])
    adj = _pick(s["adj"])
    mid = _pick(s["mid"])
    frm = _pick(s["frames"])

    nicks = []

    # 1. Fancy + frame
    nicks.append(frm.format(n=font(n, "fancy")))

    # 2. Bold italic + mid
    bi = font(n, "bold_italic")
    nicks.append(f"{mid}{bi}{mid}")

    # 3. Wide + word
    nicks.append(font(f"{w}{sep}{n}", "wide"))

    # 4. Gothic + frame
    nicks.append(_pick(s["frames"]).format(n=font(n, "gothic")))

    # 5. Double struck + mid
    nicks.append(f"{_pick(s['mid'])} {font(n, 'double')} {_pick(s['mid'])}")

    # 6. Small caps + num + frame
    sc = font(n.lower(), "small_caps")
    nicks.append(_pick(s["frames"]).format(n=f"{sc}{sep}{sn(num)}"))

    # 7. Sans bold + adj + num
    nicks.append(font(f"{n}{sep}{adj}{sep}{num}", "sans_bold"))

    # 8. Bubble + mid
    nicks.append(f"{_pick(s['mid'])}{font(n, 'bubble')}{_pick(s['mid'])}")

    # 9. Fancy word + bold name
    nicks.append(_pick(s["frames"]).format(n=f"{font(w, 'fancy')}{sep}{font(n, 'bold')}"))

    # 10. Italic + superscript
    nicks.append(f"『{font(n, 'italic')}ˢᵏʸ』")

    # 11. Mono + frame
    nicks.append(_pick(s["frames"]).format(n=font(n, "mono")))

    # 12. Multi-mid wrap
    m1, m2 = _pick(s["mid"]), _pick(s["mid"])
    nicks.append(f"꧁{m1}『{font(n, 'fancy')}』{m2}꧂")

    # 13. Num subscript
    nicks.append(_pick(s["frames"]).format(n=f"{font(n, 'bold')}{sn(num)}"))

    # 14. Double word combo
    w2 = _pick(s["words"])
    nicks.append(font(f"{w}{sep}{n}{sep}{w2}", "bold_italic"))

    # 15. Bubble + frame
    nicks.append(_pick(s["frames"]).format(n=font(n, "bubble")))

    return nicks

def gen_combo(name: str, combo_key: str) -> list[str]:
    """Kombinatsiya stil uchun niklar"""
    c   = COMBOS[combo_key]
    sk1, sk2 = c["styles"]
    s1, s2  = STYLES[sk1], STYLES[sk2]
    n   = name.strip()
    sep = _pick(SEPS)
    num = random.randint(100, 9999)
    nicks = []

    # 1–6: Maxsus frame + turli fontlar
    for frm in c["special_frames"][:6]:
        fnt = _pick(ALL_FONTS)
        nicks.append(frm.format(n=font(n, fnt)))

    # 7. Stil1 so'z + fancy name + stil2 o'rtasi
    w1  = _pick(s1["words"])
    mid2 = _pick(c["special_mid"])
    nicks.append(f"{mid2}{font(w1 + sep + n, 'fancy')}{mid2}")

    # 8. Stil2 so'z + bold italic
    w2 = _pick(s2["words"])
    nicks.append(_pick(c["special_frames"]).format(n=font(f"{n}{sep}{w2}", "bold_italic")))

    # 9. Gothic + double mid
    m1, m2 = _pick(c["special_mid"]), _pick(c["special_mid"])
    nicks.append(f"꧁{m1}{font(n, 'gothic')}{m2}꧂")

    # 10. Wide + num
    nicks.append(font(f"{n}{sep}{num}", "wide"))

    # 11. Sans bold + ikkala adj
    a1 = _pick(s1["adj"])
    a2 = _pick(s2["adj"])
    nicks.append(font(f"{a1}{sep}{n}{sep}{a2}", "sans_bold"))

    # 12. Bubble + special frame
    nicks.append(_pick(c["special_frames"]).format(n=font(n, "bubble")))

    # 13. Mono + special mid
    m3 = _pick(c["special_mid"])
    nicks.append(f"{m3}{font(n, 'mono')}{m3}")

    # 14. Double struck + frame
    nicks.append(_pick(c["special_frames"]).format(n=font(n, "double")))

    # 15. Maxsus: ikkala stildan so'z + fancy
    nicks.append(_pick(c["special_frames"]).format(
        n=font(f"{w1}{sep}{n}{sep}{w2}", "fancy")
    ))

    return nicks

def gen_mix(n1: str, n2: str) -> list[str]:
    """Ikki ismni aralashtirish"""
    n1, n2 = n1.strip(), n2.strip()
    half1 = n1[:len(n1)//2 + len(n1) % 2]
    half2 = n2[len(n2)//2:]
    nicks = []
    sep = _pick(SEPS)

    style_vals = list(STYLES.values())
    for _ in range(16):
        s   = _pick(style_vals)
        fnt = _pick(ALL_FONTS)
        frm = _pick(s["frames"])
        mid = _pick(s["mid"])
        mode = _ % 4

        if mode == 0:
            nicks.append(frm.format(n=font(half1 + half2, fnt)))
        elif mode == 1:
            nicks.append(f"{mid}{font(n1 + sep + n2, fnt)}{mid}")
        elif mode == 2:
            nicks.append(frm.format(n=font(n1, "fancy") + sep + font(n2, "gothic")))
        else:
            w = _pick(s["words"])
            nicks.append(f"{mid}{font(half1 + w + half2, fnt)}{mid}")

    return nicks

def gen_random(count: int = 10) -> list[str]:
    firsts = ["Pro","Elite","Dark","Ultra","Alpha","Omega","Neo","Hyper","Lord","God",
              "Ghost","Iron","Storm","Blade","Shadow","Void","Silver","Cosmic","Neon","Cyber"]
    lasts  = ["Wolf","Dragon","Falcon","Tiger","Phoenix","Viper","Ghost","Legend",
              "Hunter","Slayer","Knight","Rogue","Striker","Warrior","Master","Rage"]

    results = []
    for _ in range(count):
        sk  = _pick(list(STYLES.keys()))
        s   = STYLES[sk]
        nm  = _pick(firsts) + _pick(lasts)
        fnt = _pick(ALL_FONTS)
        frm = _pick(s["frames"])
        mid = _pick(s["mid"])
        num = random.randint(10, 9999)
        mode = _ % 5

        if mode == 0:
            results.append(frm.format(n=font(nm, fnt)))
        elif mode == 1:
            results.append(f"{mid}{font(nm, fnt)}{mid}")
        elif mode == 2:
            results.append(f"꧁{mid}{font(nm, fnt)}{mid}꧂")
        elif mode == 3:
            results.append(frm.format(n=font(f"{nm}{_pick(SEPS)}{num}", fnt)))
        else:
            w = _pick(s["words"])
            results.append(f"{mid}{font(w + _pick(SEPS) + nm, fnt)}{mid}")

    return results

_stats: dict[int, dict] = {}

def track(uid: int, key: str):
    d = _stats.setdefault(uid, {"gen": 0, "rand": 0, "mix": 0, "combo": 0, "styles": {}, "combos": {}})
    if key in ("gen", "rand", "mix", "combo"):
        d[key] += 1
    elif key.startswith("s:"):
        sk = key[2:]
        d["styles"][sk] = d["styles"].get(sk, 0) + 1
    elif key.startswith("c:"):
        ck = key[2:]
        d["combos"][ck] = d["combos"].get(ck, 0) + 1

def fav_style(uid: int) -> str:
    d = _stats.get(uid, {})
    fs = d.get("styles", {})
    if not fs: return "—"
    best = max(fs, key=fs.get)
    return STYLES[best]["name"]

def fav_combo(uid: int) -> str:
    d = _stats.get(uid, {})
    fc = d.get("combos", {})
    if not fc: return "—"
    best = max(fc, key=fc.get)
    return COMBOS[best]["name"]

def main_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🎨 Nik yasash"),   KeyboardButton(text="🔀 Stil kombinatsiya")],
        [KeyboardButton(text="🎲 Tasodifiy"),    KeyboardButton(text="🔁 Ismlarni aralashtir")],
        [KeyboardButton(text="📋 Barcha stillar"),KeyboardButton(text="📊 Statistika")],
        [KeyboardButton(text="ℹ️ Yordam")],
    ], resize_keyboard=True)

def styles_kb(selected: str = ""):
    rows, row = [], []
    for k, v in STYLES.items():
        mark = "✅" if k == selected else ""
        row.append(InlineKeyboardButton(text=f"{mark}{v['emoji']}{v['name'].split()[-1]}", callback_data=f"sty:{k}"))
        if len(row) == 3:
            rows.append(row); row = []
    if row: rows.append(row)
    rows.append([InlineKeyboardButton(text="🔙 Orqaga", callback_data="go:main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def combos_kb():
    rows, row = [], []
    for k, v in COMBOS.items():
        row.append(InlineKeyboardButton(text=v["name"], callback_data=f"cmb:{k}"))
        if len(row) == 2:
            rows.append(row); row = []
    if row: rows.append(row)
    rows.append([InlineKeyboardButton(text="🔙 Orqaga", callback_data="go:main")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def nick_kb(name: str, sk: str, is_combo=False):
    prefix = "cmb_regen" if is_combo else "regen"
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Yangi variantlar", callback_data=f"{prefix}:{name}:{sk}"),
            InlineKeyboardButton(text="🎨 Stil o'zgartir",   callback_data=f"chstyle:{name}"),
        ],
        [
            InlineKeyboardButton(text="🔀 Kombinatsiyaga",   callback_data=f"go_combo:{name}"),
            InlineKeyboardButton(text="🏠 Menu",             callback_data="go:main"),
        ]
    ])

def rand_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Yana 10 ta", callback_data="rand:10"),
            InlineKeyboardButton(text="🎯 Yana 5 ta",  callback_data="rand:5"),
        ],
        [InlineKeyboardButton(text="🏠 Menu", callback_data="go:main")]
    ])

def nick_list_text(nicks: list, title: str) -> str:
    t = f"{title}\n{'━'*22}\n\n"
    for i, n in enumerate(nicks, 1):
        t += f"<b>{i:02d}.</b> <code>{n}</code>\n\n"
    t += f"{'━'*22}\n💡 Nikni <b>bosib</b> nusxa oling!"
    return t


@dp.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(
        "╔═══════════════════════╗\n"
        "║  🎨  NİK  MASTER  🎨  ║\n"
        "║   Professional Bot   ║\n"
        "╚═══════════════════════╝\n\n"
        f"Salom, <b>{msg.from_user.first_name}</b>! 👋\n\n"
        "🔥 <b>12 ta stil</b> — har biri uchun 15 ta nik\n"
        "🔀 <b>10 ta kombinatsiya</b> — 2 stil birlashtiriladi\n"
        "🎲 <b>Tasodifiy</b> — har safar noyob\n"
        "🔁 <b>Mix</b> — 2 ismdan juft nik\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "👇 Quyidagi tugmalardan boshlang:",
        reply_markup=main_kb(), parse_mode="HTML"
    )

# ── YORDAM ──
@dp.message(F.text == "ℹ️ Yordam")
async def cmd_help(msg: Message):
    await msg.answer(
        "📖 <b>NİK MASTER — To'liq qo'llanma</b>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎨 <b>Nik yasash</b>\n"
        "Ismingiz + 1 ta stil → 15 ta nik\n\n"
        "🔀 <b>Stil kombinatsiya</b>\n"
        "Ismingiz + 2 ta birlashgan stil → 15 ta nik\n"
        "<i>Misol: Olov+Muz, Dark+Qirol, Ninja+Ajdaho...</i>\n\n"
        "🎲 <b>Tasodifiy niklar</b>\n"
        "Avtomatik 10 ta noyob nik\n\n"
        "🔁 <b>Ismlarni aralashtir</b>\n"
        "2 ismni aralashtirish — 16 ta variant\n"
        "<i>Misol: Ali, Vali → juft nik</i>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎭 <b>12 ta stil:</b>\n"
        "🔥 🌊 👑 💀 ⚡ 🌸 🌌 🥷 🤖 😇 🐉 🩸 🌈\n\n"
        "🔀 <b>10 ta kombinatsiya:</b>\n"
        "🔥❄️ 💀👑 🌌🤖 🥷🐉 😇💀 🌈🌌\n"
        "🩸⚡ 🔥🐉 👑🌌 🤖🌈\n\n"
        "🔤 <b>11 ta Unicode font</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 Har regeneratsiyada yangi variant!",
        reply_markup=main_kb(), parse_mode="HTML"
    )

# ── STATISTIKA ──
@dp.message(F.text == "📊 Statistika")
async def cmd_stats(msg: Message):
    uid = msg.from_user.id
    if uid not in _stats:
        return await msg.answer(
            "📊 <b>Statistika</b>\n\nHali hech narsa yo'q.\nNik yasashni boshlang! 🎨",
            reply_markup=main_kb(), parse_mode="HTML"
        )
    d = _stats[uid]
    total = d["gen"]*15 + d["rand"]*10 + d["combo"]*15 + d["mix"]*16
    await msg.answer(
        f"📊 <b>Sizning statistikangiz</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎨 Nik yasash:      <b>{d['gen']}</b> marta\n"
        f"🔀 Kombinatsiya:    <b>{d['combo']}</b> marta\n"
        f"🎲 Tasodifiy:       <b>{d['rand']}</b> marta\n"
        f"🔁 Aralashtirish:   <b>{d['mix']}</b> marta\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📦 Jami yaratilgan: <b>{total}</b> ta nik\n"
        f"❤️ Sevimli stil:    <b>{fav_style(uid)}</b>\n"
        f"🔥 Sevimli combo:   <b>{fav_combo(uid)}</b>",
        reply_markup=main_kb(), parse_mode="HTML"
    )

# ── BARCHA STILLAR ──
@dp.message(F.text == "📋 Barcha stillar")
async def cmd_all_styles(msg: Message):
    lines = ["🎭 <b>Barcha stillar (namuna):</b>\n━━━━━━━━━━━━━━━━━━━━━━\n"]
    for k, v in STYLES.items():
        sample = gen_single("Pro", k)[0]
        lines.append(f"{v['name']}\n<code>{sample}</code>\n")
    lines.append("\n🔀 <b>Kombinatsiyalar:</b>\n━━━━━━━━━━━━━━━━━━━━━━\n")
    for k, v in COMBOS.items():
        sample = gen_combo("Pro", k)[0]
        lines.append(f"{v['name']} — {v['desc']}\n<code>{sample}</code>\n")
    await msg.answer("\n".join(lines), reply_markup=main_kb(), parse_mode="HTML")

# ── NIK YASASH ──
@dp.message(F.text == "🎨 Nik yasash")
async def cmd_make(msg: Message, state: FSMContext):
    await state.set_state(S.name)
    await state.update_data(mode="single")
    await msg.answer(
        "✏️ <b>Ismingizni kiriting:</b>\n\n"
        "<i>Misol: Ali, Dragon, NightWolf...</i>\n"
        "• 2–20 ta belgi",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="❌ Bekor")]],
            resize_keyboard=True
        ), parse_mode="HTML"
    )

# ── KOMBİNATSİYA ──
@dp.message(F.text == "🔀 Stil kombinatsiya")
async def cmd_combo(msg: Message, state: FSMContext):
    await state.set_state(S.name)
    await state.update_data(mode="combo")
    await msg.answer(
        "✏️ <b>Ismingizni kiriting:</b>\n\n"
        "<i>Kombinatsiya: 2 ta stil birlashtirilib nik yasaladi</i>\n"
        "• 2–20 ta belgi",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="❌ Bekor")]],
            resize_keyboard=True
        ), parse_mode="HTML"
    )

@dp.message(S.name)
async def get_name(msg: Message, state: FSMContext):
    if msg.text == "❌ Bekor":
        await state.clear()
        return await msg.answer("🏠 Asosiy menu", reply_markup=main_kb())
    n = msg.text.strip()
    if not 2 <= len(n) <= 20:
        return await msg.answer("⚠️ Ism 2–20 ta belgi bo'lsin. Qayta kiriting:")
    data = await state.get_data()
    await state.update_data(name=n)
    mode = data.get("mode", "single")
    if mode == "combo":
        await state.set_state(S.combo_pick)
        await msg.answer(
            f"✅ Ism: <b>{n}</b>\n\n🔀 <b>Kombinatsiyani tanlang:</b>",
            reply_markup=combos_kb(), parse_mode="HTML"
        )
    else:
        await state.set_state(S.style_pick)
        await msg.answer(
            f"✅ Ism: <b>{n}</b>\n\n🎭 <b>Stilni tanlang:</b>",
            reply_markup=styles_kb(), parse_mode="HTML"
        )

# ── STİL TANLASH ──
@dp.callback_query(F.data.startswith("sty:"), S.style_pick)
async def pick_style(call: CallbackQuery, state: FSMContext):
    sk = call.data.split(":")[1]
    data = await state.get_data()
    name = data.get("name", "Pro")
    await state.clear()
    track(call.from_user.id, "gen")
    track(call.from_user.id, f"s:{sk}")
    nicks = gen_single(name, sk)
    s = STYLES[sk]
    await call.message.edit_text(
        nick_list_text(nicks, f"{s['emoji']} <b>{s['name']}</b> — <b>{name}</b>"),
        reply_markup=nick_kb(name, sk),
        parse_mode="HTML"
    )
    await call.answer()

# ── COMBO TANLASH ──
@dp.callback_query(F.data.startswith("cmb:"), S.combo_pick)
async def pick_combo(call: CallbackQuery, state: FSMContext):
    ck = call.data.split(":")[1]
    data = await state.get_data()
    name = data.get("name", "Pro")
    await state.clear()
    track(call.from_user.id, "combo")
    track(call.from_user.id, f"c:{ck}")
    nicks = gen_combo(name, ck)
    c = COMBOS[ck]
    await call.message.edit_text(
        nick_list_text(nicks, f"{c['name']} — <b>{name}</b>\n<i>{c['desc']}</i>"),
        reply_markup=nick_kb(name, ck, is_combo=True),
        parse_mode="HTML"
    )
    await call.answer()

# ── REGENERATSIYA ──
@dp.callback_query(F.data.startswith("regen:"))
async def regen(call: CallbackQuery):
    _, name, sk = call.data.split(":", 2)
    track(call.from_user.id, "gen")
    nicks = gen_single(name, sk)
    s = STYLES[sk]
    await call.message.edit_text(
        nick_list_text(nicks, f"{s['emoji']} <b>{s['name']}</b> — <b>{name}</b>"),
        reply_markup=nick_kb(name, sk),
        parse_mode="HTML"
    )
    await call.answer("✅ Yangilandi!")

@dp.callback_query(F.data.startswith("cmb_regen:"))
async def cmb_regen(call: CallbackQuery):
    _, name, ck = call.data.split(":", 2)
    track(call.from_user.id, "combo")
    nicks = gen_combo(name, ck)
    c = COMBOS[ck]
    await call.message.edit_text(
        nick_list_text(nicks, f"{c['name']} — <b>{name}</b>\n<i>{c['desc']}</i>"),
        reply_markup=nick_kb(name, ck, is_combo=True),
        parse_mode="HTML"
    )
    await call.answer("✅ Yangilandi!")

# ── STİL O'ZGARTİRİSH ──
@dp.callback_query(F.data.startswith("chstyle:"))
async def change_style(call: CallbackQuery, state: FSMContext):
    name = call.data.split(":", 1)[1]
    await state.set_state(S.style_pick)
    await state.update_data(name=name)
    await call.message.edit_text(
        f"✅ Ism: <b>{name}</b>\n\n🎭 <b>Yangi stilni tanlang:</b>",
        reply_markup=styles_kb(), parse_mode="HTML"
    )
    await call.answer()

# ── KOMBINATSIYAGA O'TISH ──
@dp.callback_query(F.data.startswith("go_combo:"))
async def go_combo(call: CallbackQuery, state: FSMContext):
    name = call.data.split(":", 1)[1]
    await state.set_state(S.combo_pick)
    await state.update_data(name=name, mode="combo")
    await call.message.edit_text(
        f"✅ Ism: <b>{name}</b>\n\n🔀 <b>Kombinatsiyani tanlang:</b>",
        reply_markup=combos_kb(), parse_mode="HTML"
    )
    await call.answer()

# ── TASODIFIY ──
@dp.message(F.text == "🎲 Tasodifiy")
async def cmd_random(msg: Message):
    track(msg.from_user.id, "rand")
    nicks = gen_random(10)
    await msg.answer(
        nick_list_text(nicks, "🎲 <b>Tasodifiy niklar</b>"),
        reply_markup=rand_kb(), parse_mode="HTML"
    )

@dp.callback_query(F.data.startswith("rand:"))
async def rand_cb(call: CallbackQuery):
    count = int(call.data.split(":")[1])
    track(call.from_user.id, "rand")
    nicks = gen_random(count)
    await call.message.edit_text(
        nick_list_text(nicks, f"🎲 <b>Tasodifiy {count} ta nik</b>"),
        reply_markup=rand_kb(), parse_mode="HTML"
    )
    await call.answer("✅ Yangilandi!")

# ── ISM ARALASHTIRISH ──
@dp.message(F.text == "🔁 Ismlarni aralashtir")
async def cmd_mix(msg: Message, state: FSMContext):
    await state.set_state(S.mix_names)
    await msg.answer(
        "🔁 <b>Ikki ismni aralashtirish</b>\n\n"
        "Ikkala ismni <b>vergul</b> bilan yuboring:\n\n"
        "<i>Misol: Ali, Vali</i>\n"
        "<i>Misol: Dragon, Phoenix</i>\n\n"
        "💑 Do'stingiz bilan juft nik uchun!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="❌ Bekor")]],
            resize_keyboard=True
        ), parse_mode="HTML"
    )

@dp.message(S.mix_names)
async def do_mix(msg: Message, state: FSMContext):
    if msg.text == "❌ Bekor":
        await state.clear()
        return await msg.answer("🏠 Asosiy menu", reply_markup=main_kb())
    parts = [p.strip() for p in msg.text.split(",")]
    if len(parts) != 2:
        return await msg.answer("⚠️ Vergul bilan 2 ta ism kiriting!\n<i>Misol: Ali, Vali</i>", parse_mode="HTML")
    n1, n2 = parts
    if not (2 <= len(n1) <= 20 and 2 <= len(n2) <= 20):
        return await msg.answer("⚠️ Har bir ism 2–20 ta belgi bo'lsin!")
    await state.clear()
    track(msg.from_user.id, "mix")
    nicks = gen_mix(n1, n2)
    await msg.answer(
        nick_list_text(nicks, f"🔁 <b>{n1} + {n2}</b> niklar"),
        reply_markup=main_kb(), parse_mode="HTML"
    )

# ── ORQAGA / BOSH MENU ──
@dp.callback_query(F.data == "go:main")
async def go_main(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.delete()
    await call.message.answer("🏠 Asosiy menu", reply_markup=main_kb())
    await call.answer()

@dp.message(F.text == "❌ Bekor")
async def cancel(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("🏠 Asosiy menu", reply_markup=main_kb())

@dp.message()
async def unknown(msg: Message):
    await msg.answer("❓ Tugmalardan foydalaning 👇", reply_markup=main_kb())

async def main():
    print("🚀 NİK MASTER v3 ishga tushdi!")
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())