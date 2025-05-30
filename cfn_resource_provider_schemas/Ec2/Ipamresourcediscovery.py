SCHEMA = {
  "typeName" : "AWS::EC2::IPAMResourceDiscovery",
  "description" : "Resource Schema of AWS::EC2::IPAMResourceDiscovery Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ipam.git",
  "definitions" : {
    "IpamOperatingRegion" : {
      "description" : "The regions IPAM Resource Discovery is enabled for. Allows for monitoring.",
      "type" : "object",
      "properties" : {
        "RegionName" : {
          "type" : "string",
          "description" : "The name of the region."
        }
      },
      "required" : [ "RegionName" ],
      "additionalProperties" : False
    },
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
    "IpamResourceDiscoveryOrganizationalUnitExclusion" : {
      "description" : "If your IPAM is integrated with AWS Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion.",
      "type" : "object",
      "properties" : {
        "OrganizationsEntityPath" : {
          "type" : "string",
          "description" : "An AWS Organizations entity path. Build the path for the OU(s) using AWS Organizations IDs separated by a '/'. Include all child OUs by ending the path with '/*'.",
          "minLength" : 1
        }
      },
      "required" : [ "OrganizationsEntityPath" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "IpamResourceDiscoveryId" : {
      "description" : "Id of the IPAM Pool.",
      "type" : "string"
    },
    "OwnerId" : {
      "description" : "Owner Account ID of the Resource Discovery",
      "type" : "string"
    },
    "OperatingRegions" : {
      "description" : "The regions Resource Discovery is enabled for. Allows resource discoveries to be created in these regions, as well as enabling monitoring",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/IpamOperatingRegion"
      }
    },
    "IpamResourceDiscoveryRegion" : {
      "description" : "The region the resource discovery is setup in. ",
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "OrganizationalUnitExclusions" : {
      "description" : "A set of organizational unit (OU) exclusions for this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/IpamResourceDiscoveryOrganizationalUnitExclusion"
      }
    },
    "IsDefault" : {
      "description" : "Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.",
      "type" : "boolean"
    },
    "IpamResourceDiscoveryArn" : {
      "description" : "Amazon Resource Name (Arn) for the Resource Discovery.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of this Resource Discovery.",
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
  "propertyTransform" : { },
  "required" : [ ],
  "primaryIdentifier" : [ "/properties/IpamResourceDiscoveryId" ],
  "readOnlyProperties" : [ "/properties/IpamResourceDiscoveryId", "/properties/IpamResourceDiscoveryArn", "/properties/OwnerId", "/properties/IpamResourceDiscoveryRegion", "/properties/IsDefault", "/properties/State" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateIpamResourceDiscovery", "ec2:DescribeIpamResourceDiscoveries", "ec2:ModifyIpamResourceDiscovery", "ec2:CreateTags", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeIpamResourceDiscoveries" ]
    },
    "update" : {
      "permissions" : [ "ec2:ModifyIpamResourceDiscovery", "ec2:DescribeIpamResourceDiscoveries", "ec2:CreateTags", "ec2:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteIpamResourceDiscovery", "ec2:DescribeIpamResourceDiscoveries", "ec2:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeIpamResourceDiscoveries" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:DeleteTags", "ec2:CreateTags" ]
  }
}