#!/usr/bin/env python3

import os,sys
from fabric.api import local, lcd

command_list = [
  'yarn fix-lint-errors -- src/components/HelloComponent',
  # 'yarn fix-lint-errors -- src/components/BottomBar',
  # 'yarn fix-lint-errors -- src/components/BottomBarWithAds',
  # 'yarn fix-lint-errors -- src/components/BottomNavigationMenu',

  # 'yarn fix-lint-errors -- src/components/Dialog/ConfirmServiceRequestDialog',
  # 'yarn fix-lint-errors -- src/components/Dialog/DebugDialog',
  # 'yarn fix-lint-errors -- src/components/Dialog/HelloDialog',
  # 'yarn fix-lint-errors -- src/components/Dialog/ReservationNumberAssignedDialog',
  # 'yarn fix-lint-errors -- src/components/EscaleHorizontalScrollBar',
  # 'yarn fix-lint-errors -- src/components/EscaleMenuBody',
  # 'yarn fix-lint-errors -- src/components/EscaleMenuList',
  # 'yarn fix-lint-errors -- src/components/EscaleUserInfo',
  # 'yarn fix-lint-errors -- src/components/FoodDetailDialog',
  # 'yarn fix-lint-errors -- src/components/FoodMenuBody',
  # 'yarn fix-lint-errors -- src/components/FoodMenuListingCategoryScrollBar',
  # 'yarn fix-lint-errors -- src/components/FoodMenuListingPageAd',
  # 'yarn fix-lint-errors -- src/components/FoodMenuListingPageAdTapToFoodDetail',
  # 'yarn fix-lint-errors -- src/components/FoodMenuListingPageAdTapToHighlightCategories',
  # 'yarn fix-lint-errors -- src/components/FoodPhoto',
  # 'yarn fix-lint-errors -- src/components/FullScreenAdPicture',
  # 'yarn fix-lint-errors -- src/components/FullScreenLoading',
  # 'yarn fix-lint-errors -- src/components/HelloComponent',
  # 'yarn fix-lint-errors -- src/components/Helloworld',
  # 'yarn fix-lint-errors -- src/components/HelloworldDialog',
  # 'yarn fix-lint-errors -- src/components/HorizontalScrollbar',
  # 'yarn fix-lint-errors -- src/components/LynkedLogoJsx',
  # 'yarn fix-lint-errors -- src/components/LynkedLogoSvg',

  # 'yarn fix-lint-errors -- src/components/Meny-light/BottomAdsContainer',
  # 'yarn fix-lint-errors -- src/components/Meny-light/BottomAdsTapToFoodDetail',
  # 'yarn fix-lint-errors -- src/components/Meny-light/FoodDetailDialog',
  # 'yarn fix-lint-errors -- src/components/Meny-light/FoodMenuBody',
  # 'yarn fix-lint-errors -- src/components/Meny-light/Helloworld',
  # 'yarn fix-lint-errors -- src/components/Meny-light/RestaurantBar',
  # 'yarn fix-lint-errors -- src/components/Meny/BottomAdsTapToFoodDetail',
  # 'yarn fix-lint-errors -- src/components/Meny/EscaleHorizontalScrollBar',
  # 'yarn fix-lint-errors -- src/components/Meny/FoodDetailDialog',
  # 'yarn fix-lint-errors -- src/components/Meny/FoodMenuAdvertisementWindow',
  # 'yarn fix-lint-errors -- src/components/Meny/HorizontalScrollBar',
  # 'yarn fix-lint-errors -- src/components/Meny/OrderListAdvertisementWindow',
  # 'yarn fix-lint-errors -- src/components/Meny/RestaurantBarWithBackButton',
  # 'yarn fix-lint-errors -- src/components/Meny/RestaurantLogo',
  # 'yarn fix-lint-errors -- src/components/Meny/RubbishBinButton',
  # 'yarn fix-lint-errors -- src/components/Meny/TapToFoodCategory',
  # 'yarn fix-lint-errors -- src/components/Meny/TapToFoodDetail',
  # 'yarn fix-lint-errors -- src/components/NamePlate',
  # 'yarn fix-lint-errors -- src/components/OrderHistoryBody',
  # 'yarn fix-lint-errors -- src/components/OrderHistoryItem',
  # 'yarn fix-lint-errors -- src/components/OrderHistoryTotal',
  # 'yarn fix-lint-errors -- src/components/OrderListCheckoutButton',
  # 'yarn fix-lint-errors -- src/components/RestaurantBar',
  # 'yarn fix-lint-errors -- src/components/RestaurantBarWithBackButton',
  # 'yarn fix-lint-errors -- src/components/RestaurantBrandPlate',
  # 'yarn fix-lint-errors -- src/components/RestaurantLogo',
  # 'yarn fix-lint-errors -- src/components/ShowDebug',
  # 'yarn fix-lint-errors -- src/components/ShowDebugJson',
  # 'yarn fix-lint-errors -- src/components/ShowYen',
  # 'yarn fix-lint-errors -- src/components/SoldOutLabel',
  # 'yarn fix-lint-errors -- src/components/SorryWeAreClosedDialog',
  # 'yarn fix-lint-errors -- src/components/SquareLinkedLogo',
  # 'yarn fix-lint-errors -- src/components/TestButton',
  'yarn fix-lint-errors -- src/components/ThinNamePlate',
  'yarn fix-lint-errors -- src/components/ToFullScreenAdPicture',
]

test_list = [
  'yarn test --maxWorkers=3 --watchAll=false'
]

with lcd("/home/logic/_workspace/LynkedKK/lynked-demo-tryout/meny-light-demo/meny-client"):
  for command in command_list:
    print(f'run {command}:')
    local(command, capture=True)

    for test_command in test_list:
      try:
        print(f'run test {test_command}:')
        local(f'{test_command}')
        local('git add /home/logic/_workspace/LynkedKK/lynked-demo-tryout/meny-light-demo/meny-client')

        print(f'{command} done.')
      except:
        print(f'failed {test_command}')
        raise e
