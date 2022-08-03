from eth_utils import address


TOKEN_ABI = """
    [
        {"constant": true,"inputs": [],"name": "decimals","outputs": [{"internalType": "uint8","name": "","type": "uint8"}],"payable": false,"stateMutability": "view","type": "function"},
        {"constant": true,"inputs": [],"name": "symbol","outputs": [{"internalType": "string","name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},
        {"constant":true,"inputs":[{"name":"src","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}
    ]
"""

VOTE_PROXY_FACTORY_V1_ABI = """
    [
        {"constant":false,"inputs":[],"name":"linkSelf","outputs":[{"name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[{"name":"hot","type":"address"}],"name":"initiateLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[{"name":"guy","type":"address"}],"name":"hasProxy","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"name":"","type":"address"}],"name":"hotMap","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"name":"","type":"address"}],"name":"linkRequests","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[],"name":"breakLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[{"name":"","type":"address"}],"name":"coldMap","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"name":"cold","type":"address"}],"name":"approveLink","outputs":[{"name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"chief","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"inputs":[{"name":"chief_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},
        {"anonymous":false,"inputs":[{"indexed":true,"name":"cold","type":"address"},{"indexed":true,"name":"hot","type":"address"}],"name":"LinkRequested","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"name":"cold","type":"address"},{"indexed":true,"name":"hot","type":"address"},{"indexed":true,"name":"voteProxy","type":"address"}],"name":"LinkConfirmed","type":"event"}
    ]
"""

VOTE_PROXY_FACTORY_V2_ABI = """
    [
        {"inputs":[{"internalType":"address","name":"chief_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"cold","type":"address"},{"indexed":true,"internalType":"address","name":"hot","type":"address"},{"indexed":true,"internalType":"address","name":"voteProxy","type":"address"}],"name":"LinkConfirmed","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"cold","type":"address"},{"indexed":true,"internalType":"address","name":"hot","type":"address"}],"name":"LinkRequested","type":"event"},
        {"constant":false,"inputs":[{"internalType":"address","name":"cold","type":"address"}],"name":"approveLink","outputs":[{"internalType":"contract VoteProxy","name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[],"name":"breakLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"chief","outputs":[{"internalType":"contract ChiefLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"coldMap","outputs":[{"internalType":"contract VoteProxy","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"hasProxy","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"hotMap","outputs":[{"internalType":"contract VoteProxy","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"internalType":"address","name":"hot","type":"address"}],"name":"initiateLink","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"linkRequests","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[],"name":"linkSelf","outputs":[{"internalType":"contract VoteProxy","name":"voteProxy","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"}
    ]
"""

VOTE_PROXY_ABI = """
    [
        {"constant":true,"inputs":[],"name":"gov","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":true,"inputs":[],"name":"cold","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[],"name":"freeAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"iou","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"hot","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
        {"constant":true,"inputs":[],"name":"chief","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
        {"inputs":[{"name":"_chief","type":"address"},{"name":"_cold","type":"address"},{"name":"_hot","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}
    ]
"""

MKR = "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"
IOU_1_0 = "0x9aed7a25f2d928225e6fb2388055c7363ad6727b"

IOUs = dict(
    IOU_1_1="0x496c67a4ced9c453a60f3166ab4b329870c8e355",
    IOU_1_2="0xa618e54de493ec29432ebd2ca7f14efbf6ac17f7",
)

VOTE_PROXY_FACTORIES = [
    dict(
        address="0x6fcd258af181b3221073a96dd90d1f7ae7eec408",
        abi=VOTE_PROXY_FACTORY_V2_ABI,
        iou=IOUs["IOU_1_2"],
        chief_address="0x0a3f6849f78076aefadf113f5bed87720274ddc0",
        chief_abi="""[{"constant":true,"inputs":[],"name":"IOU","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"getUserRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"GOV","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"getCapabilityRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"isCapabilityPublic","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_YAYS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"whom","type":"address"}],"name":"lift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"etch","outputs":[{"name":"slate","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"approvals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"},{"name":"enabled","type":"bool"}],"name":"setUserRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"role","type":"uint8"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setRoleCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"}],"name":"hasUserRole","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caller","type":"address"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"canCall","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"slates","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setPublicCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"enabled","type":"bool"}],"name":"setRootUser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"votes","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"isUserRoot","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"deposits","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hat","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"GOV","type":"address"},{"name":"IOU","type":"address"},{"name":"MAX_YAYS","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"slate","type":"bytes32"}],"name":"Etch","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]""",
    ),
    dict(
        address="0x868ba9aeaca5b73c7c27f3b01588bf4f1339f2bc",
        abi=VOTE_PROXY_FACTORY_V1_ABI,
        iou=IOUs["IOU_1_1"],
        chief_address="0x9ef05f7f6deb616fd37ac3c959a2ddd25a54e4f5",
        chief_abi="""[{"constant":true,"inputs":[],"name":"IOU","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"getUserRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"GOV","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"getCapabilityRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"isCapabilityPublic","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_YAYS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"whom","type":"address"}],"name":"lift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"etch","outputs":[{"name":"slate","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"approvals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"},{"name":"enabled","type":"bool"}],"name":"setUserRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"role","type":"uint8"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setRoleCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"}],"name":"hasUserRole","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caller","type":"address"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"canCall","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"slates","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setPublicCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"enabled","type":"bool"}],"name":"setRootUser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"votes","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"isUserRoot","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"deposits","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hat","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"GOV","type":"address"},{"name":"IOU","type":"address"},{"name":"MAX_YAYS","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"slate","type":"bytes32"}],"name":"Etch","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]""",
    ),
]

CHIEFS = [
    dict(
        address="0x0a3f6849f78076aefadf113f5bed87720274ddc0",
        abi="""[{"inputs":[{"internalType":"contract DSToken","name":"GOV","type":"address"},{"internalType":"contract DSToken","name":"IOU","type":"address"},{"internalType":"uint256","name":"MAX_YAYS","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"slate","type":"bytes32"}],"name":"Etch","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"guy","type":"address"},{"indexed":true,"internalType":"bytes32","name":"foo","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"bar","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"},{"constant":true,"inputs":[],"name":"GOV","outputs":[{"internalType":"contract DSToken","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"IOU","outputs":[{"internalType":"contract DSToken","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_YAYS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"approvals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"internalType":"contract DSAuthority","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"caller","type":"address"},{"internalType":"address","name":"code","type":"address"},{"internalType":"bytes4","name":"sig","type":"bytes4"}],"name":"canCall","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"deposits","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address[]","name":"yays","type":"address[]"}],"name":"etch","outputs":[{"internalType":"bytes32","name":"slate","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"code","type":"address"},{"internalType":"bytes4","name":"sig","type":"bytes4"}],"name":"getCapabilityRoles","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"who","type":"address"}],"name":"getUserRoles","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"who","type":"address"},{"internalType":"uint8","name":"role","type":"uint8"}],"name":"hasUserRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hat","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"code","type":"address"},{"internalType":"bytes4","name":"sig","type":"bytes4"}],"name":"isCapabilityPublic","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"who","type":"address"}],"name":"isUserRoot","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"last","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"launch","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"whom","type":"address"}],"name":"lift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"live","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"contract DSAuthority","name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"code","type":"address"},{"internalType":"bytes4","name":"sig","type":"bytes4"},{"internalType":"bool","name":"enabled","type":"bool"}],"name":"setPublicCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint8","name":"role","type":"uint8"},{"internalType":"address","name":"code","type":"address"},{"internalType":"bytes4","name":"sig","type":"bytes4"},{"internalType":"bool","name":"enabled","type":"bool"}],"name":"setRoleCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"who","type":"address"},{"internalType":"bool","name":"enabled","type":"bool"}],"name":"setRootUser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"who","type":"address"},{"internalType":"uint8","name":"role","type":"uint8"},{"internalType":"bool","name":"enabled","type":"bool"}],"name":"setUserRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"slates","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address[]","name":"yays","type":"address[]"}],"name":"vote","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"votes","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"}]""",
    ),
    dict(
        address="0x9ef05f7f6deb616fd37ac3c959a2ddd25a54e4f5",
        abi="""[{"constant":true,"inputs":[],"name":"IOU","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"getUserRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"GOV","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"getCapabilityRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"isCapabilityPublic","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_YAYS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"whom","type":"address"}],"name":"lift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"etch","outputs":[{"name":"slate","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"approvals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"},{"name":"enabled","type":"bool"}],"name":"setUserRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"role","type":"uint8"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setRoleCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"}],"name":"hasUserRole","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caller","type":"address"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"canCall","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"slates","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setPublicCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"enabled","type":"bool"}],"name":"setRootUser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"votes","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"isUserRoot","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"deposits","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hat","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"GOV","type":"address"},{"name":"IOU","type":"address"},{"name":"MAX_YAYS","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"slate","type":"bytes32"}],"name":"Etch","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]""",
    ),
]
