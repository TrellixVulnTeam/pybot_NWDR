#this script to demo create default scene data (game map)
import jsonpickle
from GameModels.SceneConnectionData import SceneConnectionData
from GameModels.SceneData import SceneData

listDefaultScene = list()
default_scene_data_path = 'db/defaultscene/default_scene.json'

#start scene 1
listDefaultScene.append(
    SceneData(
        0,
        'In the living room.',
        'You are standing in an living room of a house.' +
        ' There is a small mailbox on the table here.',
        -1,
        [],
        [
            SceneConnectionData(1, ['take mailbox']),
            SceneConnectionData(6, ['go out', 'go outside'])
        ],
        'You can \'take mailbox\' to find a key.'
    )
)

listDefaultScene.append(
    SceneData(
        1,
        'You taked the mailbox.',
        'Do you want to Open it?',
        -1,
        [],
        [
            SceneConnectionData(0, ['no', 'drop mailbox', 'throw mailbox', 'drop the mailbox', 'throw the mailbox']),
            SceneConnectionData(2, ['open', 'yes', 'open the mailbox', 'open mailbox']),
            SceneConnectionData(6, ['go out', 'go outside'])
        ],
        'Just \'open\' it!'
    )
)

listDefaultScene.append(
    SceneData(
        2,
        'Opening the mailbox ...',
        'Opening the small mailbox reveals a leaflet and a key.',
        -1,
        [],
        [
            SceneConnectionData(3, ['y', 'yes', 'read leaflet', 'read the leaflet', 'read']),
            SceneConnectionData(6, ['go out', 'go outside']),
            SceneConnectionData(5, ['take key','take the key'])
        ],
        'You can \'take key\' to go out or \'read leaflet\' to get infomation.'
    )
)

listDefaultScene.append(
    SceneData(
        3,
        'Reading...',
        'WELCOME TO PyZORK! \n' +
        'PyZORK is a game of adventure, danger, and cunning.\n' +
        'In it you will explore some of the most amazing territory ever seen by mortals to find 5 TREASURES of NATRURE ELEMENTS.\n' +
        'Let the adventure begin!',
        -1,
        [],
        [
            SceneConnectionData(4, ['drop leaflet', 'drop mailbox']),
            SceneConnectionData(6, ['go out', 'go outside']),
            SceneConnectionData(5, ['take key','take the key'])
        ],
        ';) \'take key\' to go out.'
    )
)

listDefaultScene.append(
    SceneData(
        4,
        'Droped the mailbox',
        'You drop the mailbox and thinking about the adventure.',
        -1,
        [],
        [
            SceneConnectionData(3, ['take the leaflet', 'read the leaflet', 'take leaflet', 'read leaflet', 'take mailbox', 'read mailbox']),
            SceneConnectionData(5, ['take key','take the key']),
            SceneConnectionData(6, ['go out', 'go outside'])
        ],
        ';) \'take key\' to go out.'
    )
)

listDefaultScene.append(
    SceneData(
        5,
        'You taked the key!',
        'The key can open the door then go out!',
        5,
        [],
        [
            SceneConnectionData(6, ['go out', 'go outside'])
        ],
        '\'go out\' to collect 5 nature elements!'
    )
)

listDefaultScene.append(
    SceneData(
        6,
        'Outsite of the house.',
        'You are in front of the house. In the village. ' + '\n' +
        'A path leads into the Forest to the East.',
        -1,
        [5],
        [
            SceneConnectionData(0, ['back', 'insite the house', 'back room']),
            SceneConnectionData(7, ['go east', 'east']),
            SceneConnectionData(16, ['find the alchemist', 'find alchemist'])
        ],
        '\'go east\' to find the Wood Element. \'find alchemist\' if you have Fire Element.'
    )
)
#end scene 1

#start scene 2
listDefaultScene.append(
    SceneData(
        7,
        'At the Forest Path.',
        'This is a path winding through a dimly lit forest. ' + '\n' +
        'There is a large tree with some low branches stands at the end of the path.' +
        '\nKeep go East you can see a River, something great waiting for you.',
        -1,
        [],
        [
            SceneConnectionData(8, ['find the tree', 'find large tree']),
            SceneConnectionData(6, ['back', 'back to village']),
            SceneConnectionData(11, ['go e', 'go east', 'east'])
        ],
        '\'find large tree\' to see the Wood Element. \'go east\' to get the Water Element.'
    )
)

listDefaultScene.append(
    SceneData(
        8,
        'Behide the Large Tree.',
        'It is the tallest Tree in this Forest. Something waiting for you on top of the Tree.',
        -1,
        [],
        [
            SceneConnectionData(9, ['climb tree', 'climb the tree']),
            SceneConnectionData(7, ['back']),
            SceneConnectionData(11, ['go e', 'go east', 'east'])
        ],
        '\'climb tree\' to get the Wood. \'go east\' to the river.'
    )
)

listDefaultScene.append(
    SceneData(
        9,
        'Up the Tree.',
        'You are about 10 feet above the ground nestled among some large branches.' + '\n' +
        'The nearest branch above you is above your reach.' + '\n' +
        'Beside you on the branch is a small bird\'s nest.' + '\n' +
        'In the bird\'s nest is a large egg encrusted with precious jewels.' + '\n' +
        'WOW! It is exactly a Wood Tresure.',
        -1,
        [],
        [
            SceneConnectionData(8, ['climb down']),
            SceneConnectionData(10, ['take', 'yes', 'take it'])
        ],
        '\'take it\' then \'climb down\''
    )
)

listDefaultScene.append(
    SceneData(
        10,
        'Taked the Wood Treasure.',
        'The Wood Tresure is now in your inventory!' + '\n' +
        'You can climb down then find 4 other to win the PyZork!',
        1,
        [],
        [
            SceneConnectionData(8, ['climb down'])
        ],
        '\'climb down\' to find orther Elements.'
    )
)
#end scene 2

#start scene 3
listDefaultScene.append(
    SceneData(
        11,
        'At the Flowing River.',
        'There is a large river flowing in front of you. Something glisten inside the river with blue light. It is look like very valuable.' +
        'In the Northwest of the river, It is has a Volcano!',
        -1,
        [],
        [
            SceneConnectionData(13, ['keep going', 'keep walking', 'cross river', 'cross the river', 'go northwest']),
            SceneConnectionData(12, ['take blue light', 'take tresure', 'take gem']),
            SceneConnectionData(7, ['back'])
        ],
        '\'take gem\', it is the Water Element.'
    )
)

listDefaultScene.append(
    SceneData(
        12,
        'Insite the River.',
        'WOW! The Tresure chose you. It is really WATER TRESURE. You got it in your inventory.' +
        '\nRemember, We have to find 5 Tresures, then bring it to Temple of Nature in the South.',
        3,
        [1],
        [
            SceneConnectionData(9, ['back']),
            SceneConnectionData(13, ['keep going', 'keep walking', 'cross the river', 'cross river', 'go northwest'])
        ],
        '\'keep going\' to the northwest.'
    )
)
#end scene 3

#start scene 4
listDefaultScene.append(
    SceneData(
        13,
        'The Volcano.',
        'It is a Hurge Volcano. It is look very dangerous. On top the Volcano is a Gem with red light, shining and very precious.',
        -1,
        [1],
        [
            SceneConnectionData(11, ['back', 'back to river']),
            SceneConnectionData(14, ['climb', 'climb top', 'climb volcano'])
        ],
        '\'climb top\' of the volcano. Something hot on it.'
    )
)

listDefaultScene.append(
    SceneData(
        14,
        'Top of Volcano.',
        'You are here. The Tresure of Fire here!!!',
        -1,
        [3],
        [
            SceneConnectionData(15, ['take gem', 'take tresure'])
        ],
        '\'take gem\', the Fire Element really here.'
    )
)

listDefaultScene.append(
    SceneData(
        15,
        'Taked the Tresure!',
        'Yeah, We all know it is dangerous but you did it completely! You got the Fire Tresure.' +
        '\nTake a look, there no way to keep going. ' +
        'We need go back the village and find orther tresures. ' +
        'A alchemist is living in the village, You can ask him about the Fire and Metal Element',
        4,
        [3],
        [
            SceneConnectionData(6, ['back the village', 'back'])
        ],
        '\'back the village\' to find the Alchemist.'
    )
)
#end scene 4

#start scene 5
listDefaultScene.append(
    SceneData(
        16,
        'The house of Alchemist',
        'The Alchemist can use Power of the Fire ELement to make a Legend Sword.',
        -1,
        [4],
        [
            SceneConnectionData(6, ['back']),
            SceneConnectionData(17, ['create sword', 'make sword', 'make legend sword'])
        ],
        '\'create sword\', it can be a rare weapon to kill the Dragon King.'
    )
)

listDefaultScene.append(
    SceneData(
        17,
        'The Legend Sword maked by the Alchemist',
        'The Legend Sword can kill Dragon King.',
        -1,
        [4],
        [
            SceneConnectionData(18, ['take the sword', 'take sword']),
            SceneConnectionData(19, ['go south', 'south'])
        ],
        'The sword is created. Now you need to \'take the sword\'.'
    )
)
listDefaultScene.append(
    SceneData(
        18,
        'You taked the Sword!',
        'Now, you need to find the Dragon King in the South to kill him, then get the Metal Element!',
        6,
        [],
        [
            SceneConnectionData(6, ['back']),
            SceneConnectionData(19, ['go south', 'south'])
        ],
        '\'go south\' to the Dragon Cave.'
    )
)
#end scene 5

#start scene 6
listDefaultScene.append(
    SceneData(
        19,
        'The Dragon Cave.',
        'A Dragon is sleeping. His breath is hot and feel death... ' +
        'The Gem on his head is the Metal Element. The only way to get it is kill him. Now try it!',
        -1,
        [6],
        [
            SceneConnectionData(20, ['kill the dragon', 'kill', 'kill dragon']),
            SceneConnectionData(21, ['kill the dragon with sword', 'kill dragon with sword']),
            SceneConnectionData(18, ['back'])
        ],
        '\'kill the dragon with sword\' to take the Metal Element.'
    )
)

listDefaultScene.append(
    SceneData(
        20,
        'You death!',
        'Remember you can not kill the Dragon without your Sword! Type OK to revive at the last scene you see the Dragon.',
        -1,
        [6],
        [
            SceneConnectionData(18, ['ok'])
        ],
        '\'ok\''
    )
)

listDefaultScene.append(
    SceneData(
        21,
        'You killed the Dragon.',
        'The Dragon was death. The Metal Element is now in your inventory.' +
        'Keep going to the Southwest, you can see a valley. Or back to the village',
        0,
        [6],
        [
            SceneConnectionData(6, ['back', 'back to village']),
            SceneConnectionData(22, ['go southwest', 'southwest', 'sw'])
        ],
        '\'go southwest\', you can see a Valley.'
    )
)
#end scene 6

#start scene 7
listDefaultScene.append(
    SceneData(
        22,
        'The Valley Here.',
        'The Valley is beautiful. The Earth Element is somewhere in the valley floor.',
        -1,
        [],
        [
            SceneConnectionData(23, ['go to the valley floor']),
            SceneConnectionData(6, ['back', 'back to village', 'back village'])
        ],
        'You can \'go to the valley floor\', something good here.'
    )
)
listDefaultScene.append(
    SceneData(
        23,
        'Valley FLoor.',
        'Standing in the Valley Floor. The Earth Element is under the ground. Need to do something...',
        -1,
        [],
        [
            SceneConnectionData(24, ['digging', 'digging ground', 'digging the ground']),
            SceneConnectionData(6, ['back', 'back to village', 'back village'])
        ],
        'You need to \'digging the ground\', Earth Element is under the ground.'
    )
)
listDefaultScene.append(
    SceneData(
        24,
        'The Earth Element here',
        'You taked the Earth Element. ' +
        'Keep going to the South, you will see the Temple of Natural. ' +
        'Then use all your 5 Element to save the Zork Kingdom.',
        2,
        [0, 3],
        [
            SceneConnectionData(6, ['back', 'back to village', 'back village']),
            SceneConnectionData(25, ['go to the temple', 'go to the south', 'go south', 'south'])
        ],
        '\'go to the south\' and see the temple. Then use all your 5 Elements'
    )
)
#end scene 7
listDefaultScene.append(
    SceneData(
        25,
        'Temple of Natural.',
        'Use your 5 elements here.',
        -1,
        [],
        [
            SceneConnectionData(26, ['use 5 elements'])
        ],
        'If you collected all 5 Element, just \'use 5 elements\' to win this game.'
    )
)
listDefaultScene.append(
    SceneData(
        26,
        'Win the game!',
        'You use the 5 Natural Elements and destroyed the pyZork. The Zork KingDoom is now reborn! \n' +
        'Use @hardreset to play pyZork again.',
        -1,
        [0, 1, 2, 3, 4],
        [],
        'Congra! You win this game. Now @hardreset to play it again without hint.'
    )
)

list_scene_json = jsonpickle.encode(listDefaultScene)
file = open(default_scene_data_path, 'w')
file.write(list_scene_json)
file.close()
print('Saved Default!')