{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "06c3a1f7-c9f9-49f6-b497-766571bda4be",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "515-394- 911\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "AREA_CODES = ['205', '251', '256', '334', '659', '938', '907', '236', '250', '778', '480', '520', \n",
    "'602', '623', '928', '327', '479', '501', '870', '209', '213', '279', '310', '323', '341', '408', \n",
    "'415', '424', '442', '510', '530', '559', '562', '619', '626', '628', '650', '657', '661', '669', \n",
    "'707', '714', '747', '760', '805', '818', '820', '831', '840', '858', '909', '916', '925', '949', \n",
    "'951', '303', '719', '720', '970', '203', '475', '860', '959', '302', '202', '239', '305', '321', \n",
    "'352', '386', '407', '448', '561', '689', '727', '754', '772', '786', '813', '850', '863', '904', \n",
    "'941', '954', '229', '404', '470', '478', '678', '706', '762', '770', '912', '808', '208', '986', \n",
    "'217', '224', '309', '312', '331', '447', '464', '618', '630', '708', '730', '773', '779', '815', \n",
    "'847', '872', '219', '260', '317', '463', '574', '765', '812', '930', '319', '515', '563', '641', \n",
    "'712', '316', '620', '785', '913', '270', '364', '502', '606', '859', '225', '318', '337', '504', \n",
    "'985', '207', '227', '240', '301', '410', '443', '667', '339', '351', '413', '508', '617', '774',\n",
    "'781', '857', '978', '231', '248', '269', '313', '517', '586', '616', '734', '810', '906', '947',\n",
    "'989', '218', '320', '507', '612', '651', '763', '952', '228', '601', '662', '769', '314', '417', \n",
    "'573', '636', '660', '816', '406', '308', '402', '531', '702', '725', '775', '603', '201', '551', \n",
    "'609', '640', '732', '848', '856', '862', '908', '973', '505', '575', '212', '315', '332', '347', \n",
    "'516', '518', '585', '607', '631', '646', '680', '716', '718', '838', '845', '914', '917', '929', \n",
    "'934', '252', '336', '704', '743', '828', '910', '919', '980', '984', '701', '216', '220', '234', \n",
    "'326', '330', '380', '419', '440', '513', '567', '614', '740', '937', '405', '539', '572', '580', \n",
    "'918', '458', '503', '541', '971', '215', '223', '267', '272', '412', '445', '484', '570', '610', \n",
    "'717', '724', '814', '878', '401', '803', '839', '843', '854', '864', '605', '423', '615', '629', \n",
    "'731', '865', '901', '931', '210', '214', '254', '281', '325', '346', '361', '409', '430', '432', \n",
    "'469', '512', '682', '713', '726', '737', '806', '817', '830', '832', '903', '915', '936', '940', \n",
    "'945', '956', '972', '979', '385', '435', '801', '802', '276', '434', '540', '571', '703', '757', \n",
    "'804', '948', '206', '253', '360', '425', '509', '564', '304', '681', '262', '274', '414', '534', \n",
    "'608', '715', '920', '307']\n",
    "\n",
    "def make_phone_number(area_codes = AREA_CODES, sep = '-'): #do not change\n",
    "    if area_codes== AREA_CODES or  area_codes == list:\n",
    "        area_codes = random.choice(area_codes)\n",
    "    else:\n",
    "        area_codes = area_codes\n",
    "    number = str(area_codes)+str(sep)+str(make_prefix())+str(sep)+str(make_suffix())\n",
    "    return (number)\n",
    "\n",
    "def make_prefix(): #do not change\n",
    "    digit1= random.choice('0123456789') #do not change or delete\n",
    "    digit2 = random.choice('0123456789') #do not change or delete\n",
    "    if(digit1== '5' and digit2 == '5'):\n",
    "        digit3= random.choice('0123456789')\n",
    "    elif(digit1 == '9' and digit2 == '5'):\n",
    "        digit3 = random.choice('023456789')\n",
    "    else:\n",
    "        digit3 = random.choice('1234567890')\n",
    "    prefix = digit1 + digit2 + digit3\n",
    "    return (prefix)\n",
    "\n",
    "def make_suffix(): #do not change\n",
    "    suffix = ' '\n",
    "    while len(suffix) < 4:\n",
    "        suffix = str(suffix) + random.choice('0123456789')\n",
    "    return (suffix)\n",
    "\n",
    "\n",
    "print (make_phone_number())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1320cdb9-04cb-4f3b-9a63-f359ba480ed8",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['540-694- 431', '347-170- 760', '326-012- 805', '404-866- 426', '310-367- 628', '616-501- 567', '530-412- 671', '980-938- 991', '640-228- 239', '435-935- 324', '331-518- 204', '812-207- 113', '214-099- 450', '970-691- 874', '810-778- 352', '734-788- 253', '731-260- 266', '580-452- 647', '507-124- 812', '302-755- 364', '747-853- 870', '469-985- 757', '279-578- 761', '727-373- 347', '320-168- 295', '413-255- 106', '540-907- 181', '830-928- 759', '603-536- 981', '208-430- 852', '734-432- 642', '202-454- 481', '442-743- 988', '458-320- 546', '864-732- 545', '747-310- 163', '848-791- 429', '304-948- 382', '279-962- 420', '262-642- 622', '336-032- 856', '339-109- 543', '864-187- 969', '732-227- 660', '516-888- 076', '615-198- 690', '858-298- 873', '815-610- 072', '616-675- 453', '603-277- 646']\n",
      "['463*348* 513', '820*165* 285', '510*667* 263', '626*016* 537', '530*292* 197', '234*547* 859', '941*736* 442', '423*945* 270', '915*664* 023', '702*302* 789', '508*041* 020', '567*321* 232', '445*397* 001', '845*128* 209', '510*059* 661', '240*483* 739', '732*496* 068', '248*098* 741', '406*512* 949', '309*132* 183', '540*614* 930', '251*709* 749', '276*345* 272', '580*378* 864', '315*423* 577', '405*326* 890', '501*737* 508', '806*032* 673', '840*150* 645', '478*562* 537', '217*458* 778', '208*514* 597', '938*645* 037', '559*385* 564', '318*768* 865', '614*646* 605', '508*408* 657', '801*392* 125', '820*436* 797', '754*679* 101', '806*856* 505', '712*227* 531', '330*007* 543', '248*226* 760', '978*961* 046', '223*003* 740', '734*370* 913', '929*340* 663', '210*813* 836', '309*565* 319']\n"
     ]
    }
   ],
   "source": [
    "#part I\n",
    "x = 0\n",
    "numberlist = []\n",
    "while x < 50:\n",
    "    new = make_phone_number()\n",
    "    numberlist += [new]\n",
    "    x += 1\n",
    "print(numberlist)\n",
    "\n",
    "\n",
    "#part II\n",
    "x=0\n",
    "numberlist=[]\n",
    "for x in range(50):\n",
    "    new = make_phone_number(sep = '*')\n",
    "    numberlist += [new]\n",
    "    x+= 1\n",
    "print(numberlist)\n",
    "\n",
    "#part III\n",
    "x=0\n",
    "number_list=[]\n",
    "while x<50:\n",
    "    new=make_phone_number(['937'],[','])\n",
    "    numberlist += [new]\n",
    "print(numberlist)\n",
    "\n",
    "#part IV\n",
    "number_list=[]\n",
    "for number in range(100):\n",
    "    new = make_phone_number(['503'])\n",
    "    numberlist+=[new]\n",
    "print(numberlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3899b75e-2e40-4b9a-b632-bf7a7307caa5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
