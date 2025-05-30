SCHEMA = {
  "typeName" : "AWS::NetworkManager::ConnectAttachment",
  "description" : "AWS::NetworkManager::ConnectAttachment Resource Type Definition",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager/aws-networkmanager-connectattachment",
  "properties" : {
    "CoreNetworkId" : {
      "description" : "ID of the CoreNetwork that the attachment will be attached to.",
      "type" : "string"
    },
    "CoreNetworkArn" : {
      "description" : "The ARN of a core network.",
      "type" : "string"
    },
    "AttachmentId" : {
      "description" : "The ID of the attachment.",
      "type" : "string"
    },
    "OwnerAccountId" : {
      "description" : "The ID of the attachment account owner.",
      "type" : "string"
    },
    "AttachmentType" : {
      "description" : "The type of attachment.",
      "type" : "string"
    },
    "State" : {
      "description" : "State of the attachment.",
      "type" : "string"
    },
    "EdgeLocation" : {
      "description" : "Edge location of the attachment.",
      "type" : "string"
    },
    "ResourceArn" : {
      "description" : "The attachment resource ARN.",
      "type" : "string"
    },
    "AttachmentPolicyRuleNumber" : {
      "description" : "The policy rule number associated with the attachment.",
      "type" : "integer"
    },
    "SegmentName" : {
      "description" : "The name of the segment attachment.",
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
    "Tags" : {
      "description" : "Tags for the attachment.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "CreatedAt" : {
      "description" : "Creation time of the attachment.",
      "type" : "string"
    },
    "UpdatedAt" : {
      "description" : "Last update time of the attachment.",
      "type" : "string"
    },
    "TransportAttachmentId" : {
      "description" : "Id of transport attachment",
      "type" : "string"
    },
    "Options" : {
      "description" : "Protocol options for connect attachment",
      "$ref" : "#/definitions/ConnectAttachmentOptions"
    }
  },
  "definitions" : {
    "ProposedSegmentChange" : {
      "description" : "The attachment to move from one segment to another.",
      "type" : "object",
      "properties" : {
        "Tags" : {
          "description" : "The list of key-value tags that changed for the segment.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
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
          "uniqueItems" : True,
          "insertionOrder" : False,
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
    },
    "ConnectAttachmentOptions" : {
      "description" : "Connect attachment options for protocol",
      "type" : "object",
      "properties" : {
        "Protocol" : {
          "type" : "string",
          "description" : "Tunnel protocol for connect attachment"
        }
      },
      "additionalProperties" : False
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
  "readOnlyProperties" : [ "/properties/CoreNetworkArn", "/properties/CreatedAt", "/properties/UpdatedAt", "/properties/AttachmentType", "/properties/State", "/properties/ResourceArn", "/properties/AttachmentId", "/properties/OwnerAccountId", "/properties/AttachmentPolicyRuleNumber", "/properties/SegmentName" ],
  "createOnlyProperties" : [ "/properties/CoreNetworkId", "/properties/EdgeLocation", "/properties/TransportAttachmentId", "/properties/Options" ],
  "primaryIdentifier" : [ "/properties/AttachmentId" ],
  "required" : [ "CoreNetworkId", "EdgeLocation", "TransportAttachmentId", "Options" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:GetConnectAttachment", "networkmanager:CreateConnectAttachment", "networkmanager:TagResource", "ec2:DescribeRegions" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetConnectAttachment" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:GetConnectAttachment", "networkmanager:ListTagsForResource", "networkmanager:TagResource", "networkmanager:UntagResource", "ec2:DescribeRegions" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:GetConnectAttachment", "networkmanager:DeleteAttachment", "ec2:DescribeRegions" ]
    },
    "list" : {
      "permissions" : [ "networkmanager:ListAttachments" ]
    }
  }
}