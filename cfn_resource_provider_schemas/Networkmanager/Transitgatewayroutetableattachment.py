SCHEMA = {
  "typeName" : "AWS::NetworkManager::TransitGatewayRouteTableAttachment",
  "description" : "AWS::NetworkManager::TransitGatewayRouteTableAttachment Resource Type definition.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager/aws-networkmanager-transitgatewayroutetableattachment",
  "definitions" : {
    "ProposedSegmentChange" : {
      "description" : "The attachment to move from one segment to another.",
      "type" : "object",
      "properties" : {
        "Tags" : {
          "description" : "The key-value tags that changed for the segment.",
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/Tag"
          }
        },
        "AttachmentPolicyRuleNumber" : {
          "description" : "The rule number in the policy document that applies to this change.",
          "type" : "integer"
        },
        "SegmentName" : {
          "description" : "The name of the segment to change.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "ProposedNetworkFunctionGroupChange" : {
      "description" : "The attachment to move from one network function group to another.",
      "type" : "object",
      "properties" : {
        "Tags" : {
          "description" : "The key-value tags that changed for the network function group.",
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/Tag"
          }
        },
        "AttachmentPolicyRuleNumber" : {
          "description" : "The rule number in the policy document that applies to this change.",
          "type" : "integer"
        },
        "NetworkFunctionGroupName" : {
          "description" : "The name of the network function group to change.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "insertionOrder" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "PeeringId" : {
      "description" : "The Id of peering between transit gateway and core network.",
      "type" : "string"
    },
    "TransitGatewayRouteTableArn" : {
      "description" : "The Arn of transit gateway route table.",
      "type" : "string"
    },
    "CoreNetworkId" : {
      "description" : "The ID of a core network where you're creating a site-to-site VPN attachment.",
      "type" : "string"
    },
    "CoreNetworkArn" : {
      "description" : "The ARN of a core network for the VPC attachment.",
      "type" : "string"
    },
    "AttachmentId" : {
      "description" : "The ID of the attachment.",
      "type" : "string"
    },
    "OwnerAccountId" : {
      "description" : "Owner account of the attachment.",
      "type" : "string"
    },
    "AttachmentType" : {
      "description" : "The type of attachment.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the attachment.",
      "type" : "string"
    },
    "EdgeLocation" : {
      "description" : "The Region where the edge is located.",
      "type" : "string"
    },
    "ResourceArn" : {
      "description" : "The ARN of the Resource.",
      "type" : "string"
    },
    "AttachmentPolicyRuleNumber" : {
      "description" : "The policy rule number associated with the attachment.",
      "type" : "integer"
    },
    "SegmentName" : {
      "description" : "The name of the segment that attachment is in.",
      "type" : "string"
    },
    "ProposedSegmentChange" : {
      "description" : "The attachment to move from one segment to another.",
      "$ref" : "#/definitions/ProposedSegmentChange"
    },
    "NetworkFunctionGroupName" : {
      "description" : "The name of the network function group attachment.",
      "type" : "string"
    },
    "ProposedNetworkFunctionGroupChange" : {
      "description" : "The attachment to move from one network function group to another.",
      "$ref" : "#/definitions/ProposedNetworkFunctionGroupChange"
    },
    "CreatedAt" : {
      "description" : "Creation time of the attachment.",
      "type" : "string"
    },
    "UpdatedAt" : {
      "description" : "Last update time of the attachment.",
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
  "required" : [ "PeeringId", "TransitGatewayRouteTableArn" ],
  "createOnlyProperties" : [ "/properties/PeeringId", "/properties/TransitGatewayRouteTableArn" ],
  "readOnlyProperties" : [ "/properties/CoreNetworkArn", "/properties/CoreNetworkId", "/properties/CreatedAt", "/properties/UpdatedAt", "/properties/AttachmentType", "/properties/State", "/properties/ResourceArn", "/properties/AttachmentId", "/properties/OwnerAccountId", "/properties/EdgeLocation", "/properties/AttachmentPolicyRuleNumber", "/properties/SegmentName" ],
  "primaryIdentifier" : [ "/properties/AttachmentId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:CreateTransitGatewayRouteTableAttachment", "networkmanager:GetTransitGatewayRouteTableAttachment", "networkmanager:TagResource", "iam:CreateServiceLinkedRole", "ec2:DescribeRegions" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetTransitGatewayRouteTableAttachment" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:GetTransitGatewayRouteTableAttachment", "networkmanager:ListTagsForResource", "networkmanager:TagResource", "networkmanager:UntagResource", "ec2:DescribeRegions" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:GetTransitGatewayRouteTableAttachment", "networkmanager:DeleteAttachment", "ec2:DescribeRegions" ]
    },
    "list" : {
      "permissions" : [ "networkmanager:ListAttachments" ]
    }
  }
}