//
//  ActivityTableViewCell.swift
//  X-Mates
//
//  Created by Jiangyu Mao on 5/8/16.
//  Copyright © 2016 CloudGroup. All rights reserved.
//

import UIKit

class ActivityTableViewCell: UITableViewCell {

	@IBOutlet weak var dateLabel: UILabel!
	@IBOutlet weak var typeLabel: UILabel!
	
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
