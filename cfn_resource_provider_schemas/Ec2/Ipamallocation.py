SCHEMA = {
  "typeName" : "AWS::EC2::IPAMAllocation",
  "description" : "Resource Schema of AWS::EC2::IPAMAllocation Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Cidr" : {
      "description" : "Represents an IPAM custom allocation of a single IPv4 or IPv6 CIDR",
      "type" : "string"
    }
  },
  "properties" : {
    "IpamPoolAllocationId" : {
      "description" : "Id of the allocation.",
      "type" : "string"
    },
    "IpamPoolId" : {
      "description" : "Id of the IPAM Pool.",
      "type" : "string"
    },
    "Cidr" : {
      "$ref" : "#/definitions/Cidr"
    },
    "NetmaskLength" : {
      "description" : "The desired netmask length of the allocation. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.",
      "type" : "integer"
    },
    "Description" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "IpamPoolId" ],
  "primaryIdentifier" : [ "/properties/IpamPoolId", "/properties/IpamPoolAllocationId", "/properties/Cidr" ],
  "createOnlyProperties" : [ "/properties/IpamPoolId", "/properties/Cidr", "/properties/Description", "/properties/NetmaskLength" ],
  "readOnlyProperties" : [ "/properties/IpamPoolAllocationId" ],
  "writeOnlyProperties" : [ "/properties/NetmaskLength" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AllocateIpamPoolCidr", "ec2:GetIpamPoolAllocations" ]
    },
    "read" : {
      "permissions" : [ "ec2:GetIpamPoolAllocations" ]
    },
    "delete" : {
      "permissions" : [ "ec2:ReleaseIpamPoolAllocation" ]
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
      "permissions" : [ "ec2:GetIpamPoolAllocations" ]
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  }
}