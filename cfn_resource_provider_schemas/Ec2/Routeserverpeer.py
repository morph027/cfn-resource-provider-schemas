SCHEMA = {
  "typeName" : "AWS::EC2::RouteServerPeer",
  "description" : "VPC Route Server Peer",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
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
    },
    "BgpOptions" : {
      "description" : "BGP Options",
      "type" : "object",
      "properties" : {
        "PeerAsn" : {
          "description" : "BGP ASN of the Route Server Peer",
          "type" : "integer",
          "format" : "int64",
          "minimum" : 1,
          "maximum" : 4294967294
        },
        "PeerLivenessDetection" : {
          "description" : "BGP Liveness Detection",
          "type" : "string",
          "enum" : [ "bfd", "bgp-keepalive" ]
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "RouteServerId" : {
      "description" : "Route Server ID",
      "type" : "string"
    },
    "RouteServerEndpointId" : {
      "description" : "Route Server Endpoint ID",
      "type" : "string"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the Route Server Peer.",
      "type" : "string"
    },
    "Id" : {
      "description" : "The ID of the Route Server Peer.",
      "type" : "string"
    },
    "SubnetId" : {
      "description" : "Subnet ID",
      "type" : "string"
    },
    "VpcId" : {
      "description" : "VPC ID",
      "type" : "string"
    },
    "EndpointEniId" : {
      "description" : "Elastic Network Interface ID owned by the Route Server Endpoint",
      "type" : "string"
    },
    "EndpointEniAddress" : {
      "description" : "Elastic Network Interface IP address owned by the Route Server Endpoint",
      "type" : "string"
    },
    "PeerAddress" : {
      "description" : "IP address of the Route Server Peer",
      "type" : "string"
    },
    "BgpOptions" : {
      "$ref" : "#/definitions/BgpOptions"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "RouteServerEndpointId", "PeerAddress", "BgpOptions" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/RouteServerId", "/properties/EndpointEniId", "/properties/EndpointEniAddress", "/properties/SubnetId", "/properties/VpcId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/RouteServerEndpointId", "/properties/PeerAddress", "/properties/BgpOptions" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DescribeTags", "ec2:DeleteTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateRouteServerPeer", "ec2:CreateTags", "ec2:DescribeRouteServerPeers", "ec2:AuthorizeSecurityGroupIngress" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeRouteServerPeers", "ec2:DescribeTags" ]
    },
    "update" : {
      "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags", "ec2:DescribeRouteServerPeers", "ec2:DescribeTags", "ec2:ModifyRouteServerPeer" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DescribeTags", "ec2:DescribeRouteServerPeers", "ec2:DeleteRouteServerPeer", "ec2:DeleteTags", "ec2:RevokeSecurityGroupIngress" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeTags", "ec2:DescribeRouteServerPeers" ]
    }
  }
}