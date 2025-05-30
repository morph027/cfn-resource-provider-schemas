SCHEMA = {
  "typeName" : "AWS::NetworkManager::ConnectPeer",
  "description" : "AWS::NetworkManager::ConnectPeer Resource Type Definition.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager/aws-networkmanager-connectpeer",
  "properties" : {
    "PeerAddress" : {
      "description" : "The IP address of the Connect peer.",
      "type" : "string"
    },
    "CoreNetworkAddress" : {
      "description" : "The IP address of a core network.",
      "type" : "string"
    },
    "BgpOptions" : {
      "description" : "Bgp options for connect peer.",
      "$ref" : "#/definitions/BgpOptions"
    },
    "InsideCidrBlocks" : {
      "description" : "The inside IP addresses used for a Connect peer configuration.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "CoreNetworkId" : {
      "description" : "The ID of the core network.",
      "type" : "string"
    },
    "ConnectAttachmentId" : {
      "description" : "The ID of the attachment to connect.",
      "type" : "string"
    },
    "ConnectPeerId" : {
      "description" : "The ID of the Connect peer.",
      "type" : "string"
    },
    "EdgeLocation" : {
      "description" : "The Connect peer Regions where edges are located.",
      "type" : "string"
    },
    "State" : {
      "description" : "State of the connect peer.",
      "type" : "string"
    },
    "CreatedAt" : {
      "description" : "Connect peer creation time.",
      "type" : "string"
    },
    "Configuration" : {
      "description" : "Configuration of the connect peer.",
      "$ref" : "#/definitions/ConnectPeerConfiguration"
    },
    "SubnetArn" : {
      "description" : "The subnet ARN for the connect peer.",
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
  "definitions" : {
    "ConnectPeerConfiguration" : {
      "type" : "object",
      "properties" : {
        "CoreNetworkAddress" : {
          "description" : "The IP address of a core network.",
          "type" : "string"
        },
        "PeerAddress" : {
          "description" : "The IP address of the Connect peer.",
          "type" : "string"
        },
        "InsideCidrBlocks" : {
          "description" : "The inside IP addresses used for a Connect peer configuration.",
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Protocol" : {
          "$ref" : "#/definitions/TunnelProtocol"
        },
        "BgpConfigurations" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/ConnectPeerBgpConfiguration"
          }
        }
      },
      "additionalProperties" : False
    },
    "TunnelProtocol" : {
      "description" : "The protocol used for a Connect peer configuration.",
      "type" : "string"
    },
    "BgpOptions" : {
      "description" : "Bgp options",
      "type" : "object",
      "properties" : {
        "PeerAsn" : {
          "type" : "number"
        }
      },
      "additionalProperties" : False
    },
    "ConnectPeerBgpConfiguration" : {
      "description" : "Bgp configuration for connect peer",
      "type" : "object",
      "properties" : {
        "CoreNetworkAsn" : {
          "description" : "The ASN of the Coret Network.",
          "type" : "number"
        },
        "PeerAsn" : {
          "description" : "The ASN of the Connect peer.",
          "type" : "number"
        },
        "CoreNetworkAddress" : {
          "description" : "The address of a core network.",
          "type" : "string"
        },
        "PeerAddress" : {
          "description" : "The address of a core network Connect peer.",
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
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "networkmanager:TagResource", "networkmanager:UntagResource", "networkmanager:ListTagsForResource" ]
  },
  "required" : [ "ConnectAttachmentId", "PeerAddress" ],
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/PeerAddress", "/properties/CoreNetworkAddress", "/properties/BgpOptions", "/properties/InsideCidrBlocks", "/properties/ConnectAttachmentId", "/properties/SubnetArn" ],
  "writeOnlyProperties" : [ "/properties/CoreNetworkAddress", "/properties/BgpOptions", "/properties/SubnetArn" ],
  "readOnlyProperties" : [ "/properties/ConnectPeerId", "/properties/State", "/properties/CreatedAt", "/properties/Configuration", "/properties/CoreNetworkId", "/properties/EdgeLocation" ],
  "primaryIdentifier" : [ "/properties/ConnectPeerId" ],
  "additionalIdentifiers" : [ [ "/properties/ConnectAttachmentId", "/properties/CoreNetworkAddress", "/properties/InsideCidrBlocks" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:GetConnectPeer", "networkmanager:CreateConnectPeer", "networkmanager:TagResource", "ec2:DescribeRegions" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetConnectPeer" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:GetConnectPeer", "networkmanager:ListTagsForResource", "networkmanager:TagResource", "networkmanager:UntagResource", "ec2:DescribeRegions" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:GetConnectPeer", "networkmanager:DeleteConnectPeer", "ec2:DescribeRegions" ]
    },
    "list" : {
      "permissions" : [ "networkmanager:ListConnectPeers" ]
    }
  }
}