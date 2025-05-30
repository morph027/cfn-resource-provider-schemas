SCHEMA = {
  "typeName" : "AWS::EC2::VPNGateway",
  "description" : "Specifies a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.\n For more information, see [](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag key."
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag value."
        }
      },
      "required" : [ "Value", "Key" ],
      "description" : "Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)."
    }
  },
  "properties" : {
    "VPNGatewayId" : {
      "description" : "",
      "type" : "string"
    },
    "AmazonSideAsn" : {
      "description" : "The private Autonomous System Number (ASN) for the Amazon side of a BGP session.",
      "type" : "integer",
      "format" : "int64"
    },
    "Tags" : {
      "description" : "Any tags assigned to the virtual private gateway.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Type" : {
      "description" : "The type of VPN connection the virtual private gateway supports.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Type" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags" ]
  },
  "createOnlyProperties" : [ "/properties/AmazonSideAsn", "/properties/Type" ],
  "readOnlyProperties" : [ "/properties/VPNGatewayId" ],
  "primaryIdentifier" : [ "/properties/VPNGatewayId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateVpnGateway", "ec2:DescribeVpnGateways", "ec2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeVpnGateways" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeVpnGateways", "ec2:CreateTags", "ec2:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteVpnGateway", "ec2:DescribeVpnGateways" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeVpnGateways" ]
    }
  }
}