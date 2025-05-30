SCHEMA = {
  "typeName" : "AWS::NetworkManager::TransitGatewayPeering",
  "description" : "AWS::NetworkManager::TransitGatewayPeering Resoruce Type.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager/aws-networkmanager-transitgatewaypeering",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "CoreNetworkId" : {
      "description" : "The Id of the core network that you want to peer a transit gateway to.",
      "type" : "string"
    },
    "CoreNetworkArn" : {
      "description" : "The ARN (Amazon Resource Name) of the core network that you want to peer a transit gateway to.",
      "type" : "string"
    },
    "TransitGatewayArn" : {
      "description" : "The ARN (Amazon Resource Name) of the transit gateway that you will peer to a core network",
      "type" : "string"
    },
    "TransitGatewayPeeringAttachmentId" : {
      "description" : "The ID of the TransitGatewayPeeringAttachment",
      "type" : "string"
    },
    "PeeringId" : {
      "description" : "The Id of the transit gateway peering",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the transit gateway peering",
      "type" : "string"
    },
    "EdgeLocation" : {
      "description" : "The location of the transit gateway peering",
      "type" : "string"
    },
    "ResourceArn" : {
      "description" : "The ARN (Amazon Resource Name) of the resource that you will peer to a core network",
      "type" : "string"
    },
    "OwnerAccountId" : {
      "description" : "Peering owner account Id",
      "type" : "string"
    },
    "PeeringType" : {
      "description" : "Peering type (TransitGatewayPeering)",
      "type" : "string"
    },
    "CreatedAt" : {
      "description" : "The creation time of the transit gateway peering",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "networkmanager:TagResource", "networkmanager:UntagResource", "networkmanager:ListTagsForResource" ]
  },
  "required" : [ "CoreNetworkId", "TransitGatewayArn" ],
  "readOnlyProperties" : [ "/properties/CoreNetworkArn", "/properties/PeeringId", "/properties/State", "/properties/PeeringType", "/properties/OwnerAccountId", "/properties/EdgeLocation", "/properties/ResourceArn", "/properties/CreatedAt", "/properties/TransitGatewayPeeringAttachmentId" ],
  "createOnlyProperties" : [ "/properties/CoreNetworkId", "/properties/TransitGatewayArn" ],
  "primaryIdentifier" : [ "/properties/PeeringId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:CreateTransitGatewayPeering", "networkmanager:TagResource", "networkmanager:GetTransitGatewayPeering", "iam:CreateServiceLinkedRole", "ec2:CreateTransitGatewayPeeringAttachment", "ec2:AcceptTransitGatewayPeeringAttachment", "ec2:DescribeRegions" ],
      "timeoutInMinutes" : 60
    },
    "read" : {
      "permissions" : [ "networkmanager:GetTransitGatewayPeering" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:TagResource", "networkmanager:UntagResource", "networkmanager:ListTagsForResource", "networkmanager:GetTransitGatewayPeering", "ec2:DescribeRegions" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:DeletePeering", "networkmanager:GetTransitGatewayPeering", "ec2:DescribeRegions" ],
      "timeoutInMinutes" : 60
    },
    "list" : {
      "permissions" : [ "networkmanager:ListPeerings" ]
    }
  }
}