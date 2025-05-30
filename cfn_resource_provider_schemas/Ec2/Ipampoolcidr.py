SCHEMA = {
  "typeName" : "AWS::EC2::IPAMPoolCidr",
  "description" : "Resource Schema of AWS::EC2::IPAMPoolCidr Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "IpamPoolCidrId" : {
      "description" : "Id of the IPAM Pool Cidr.",
      "type" : "string"
    },
    "IpamPoolId" : {
      "description" : "Id of the IPAM Pool.",
      "type" : "string"
    },
    "Cidr" : {
      "description" : "Represents a single IPv4 or IPv6 CIDR",
      "type" : "string"
    },
    "NetmaskLength" : {
      "description" : "The desired netmask length of the provision. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.",
      "type" : "integer"
    },
    "State" : {
      "description" : "Provisioned state of the cidr.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "IpamPoolId" ],
  "primaryIdentifier" : [ "/properties/IpamPoolId", "/properties/IpamPoolCidrId" ],
  "createOnlyProperties" : [ "/properties/IpamPoolId", "/properties/Cidr", "/properties/NetmaskLength" ],
  "readOnlyProperties" : [ "/properties/IpamPoolCidrId", "/properties/State" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:ProvisionIpamPoolCidr", "ec2:GetIpamPoolCidrs" ]
    },
    "read" : {
      "permissions" : [ "ec2:GetIpamPoolCidrs" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeprovisionIpamPoolCidr", "ec2:GetIpamPoolCidrs" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "IpamPoolId" : {
            "$ref" : "resource-schema.json#/properties/IpamPoolId"
          }
        },
        "required" : [ "IpamPoolId" ]
      },
      "permissions" : [ "ec2:GetIpamPoolCidrs" ]
    }
  }
}