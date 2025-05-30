SCHEMA = {
  "typeName" : "AWS::EC2::IPAMPool",
  "description" : "Resource Schema of AWS::EC2::IPAMPool Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ipam.git",
  "definitions" : {
    "Cidr" : {
      "description" : "Represents a single IPv4 or IPv6 CIDR",
      "type" : "string"
    },
    "ProvisionedCidr" : {
      "description" : "An address space to be inserted into this pool. All allocations must be made from this address space.",
      "type" : "object",
      "properties" : {
        "Cidr" : {
          "$ref" : "#/definitions/Cidr"
        }
      },
      "required" : [ "Cidr" ],
      "additionalProperties" : False
    },
    "SourceResource" : {
      "description" : "The resource associated with this pool's space. Depending on the ResourceType, setting a SourceResource changes which space can be provisioned in this pool and which types of resources can receive allocations",
      "type" : "object",
      "properties" : {
        "ResourceId" : {
          "type" : "string"
        },
        "ResourceType" : {
          "type" : "string"
        },
        "ResourceRegion" : {
          "type" : "string"
        },
        "ResourceOwner" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceId", "ResourceType", "ResourceRegion", "ResourceOwner" ],
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
    }
  },
  "properties" : {
    "IpamPoolId" : {
      "description" : "Id of the IPAM Pool.",
      "type" : "string"
    },
    "AddressFamily" : {
      "description" : "The address family of the address space in this pool. Either IPv4 or IPv6.",
      "type" : "string"
    },
    "AllocationMinNetmaskLength" : {
      "description" : "The minimum allowed netmask length for allocations made from this pool.",
      "type" : "integer"
    },
    "AllocationDefaultNetmaskLength" : {
      "description" : "The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.",
      "type" : "integer"
    },
    "AllocationMaxNetmaskLength" : {
      "description" : "The maximum allowed netmask length for allocations made from this pool.",
      "type" : "integer"
    },
    "AllocationResourceTags" : {
      "description" : "When specified, an allocation will not be allowed unless a resource has a matching set of tags.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the IPAM Pool.",
      "type" : "string"
    },
    "AutoImport" : {
      "description" : "Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to True, an allocation will be made automatically.",
      "type" : "boolean"
    },
    "AwsService" : {
      "description" : "Limits which service in Amazon Web Services that the pool can be used in.",
      "type" : "string",
      "enum" : [ "ec2" ]
    },
    "Description" : {
      "type" : "string"
    },
    "IpamScopeId" : {
      "description" : "The Id of the scope this pool is a part of.",
      "type" : "string"
    },
    "IpamScopeArn" : {
      "description" : "The Amazon Resource Name (ARN) of the scope this pool is a part of.",
      "type" : "string"
    },
    "IpamScopeType" : {
      "description" : "Determines whether this scope contains publicly routable space or space for a private network",
      "type" : "string",
      "enum" : [ "public", "private" ]
    },
    "IpamArn" : {
      "description" : "The Amazon Resource Name (ARN) of the IPAM this pool is a part of.",
      "type" : "string"
    },
    "Locale" : {
      "description" : "The region of this pool. If not set, this will default to \"None\" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.",
      "type" : "string"
    },
    "PoolDepth" : {
      "description" : "The depth of this pool in the source pool hierarchy.",
      "type" : "integer"
    },
    "ProvisionedCidrs" : {
      "description" : "A list of cidrs representing the address space available for allocation in this pool.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ProvisionedCidr"
      }
    },
    "PublicIpSource" : {
      "description" : "The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.",
      "type" : "string",
      "enum" : [ "byoip", "amazon" ]
    },
    "PubliclyAdvertisable" : {
      "description" : "Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.",
      "type" : "boolean"
    },
    "SourceIpamPoolId" : {
      "description" : "The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.",
      "type" : "string"
    },
    "SourceResource" : {
      "$ref" : "#/definitions/SourceResource"
    },
    "State" : {
      "description" : "The state of this pool. This can be one of the following values: \"create-in-progress\", \"create-complete\", \"modify-in-progress\", \"modify-complete\", \"delete-in-progress\", or \"delete-complete\"",
      "type" : "string",
      "enum" : [ "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", "delete-complete" ]
    },
    "StateMessage" : {
      "description" : "An explanation of how the pool arrived at it current state.",
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
  "propertyTransform" : {
    "/properties/AddressFamily" : "$lowercase(AddressFamily)"
  },
  "required" : [ "IpamScopeId", "AddressFamily" ],
  "primaryIdentifier" : [ "/properties/IpamPoolId" ],
  "readOnlyProperties" : [ "/properties/IpamPoolId", "/properties/Arn", "/properties/IpamScopeArn", "/properties/IpamScopeType", "/properties/IpamArn", "/properties/PoolDepth", "/properties/State", "/properties/StateMessage" ],
  "createOnlyProperties" : [ "/properties/IpamScopeId", "/properties/SourceIpamPoolId", "/properties/Locale", "/properties/AddressFamily", "/properties/PubliclyAdvertisable", "/properties/PublicIpSource", "/properties/AwsService", "/properties/SourceResource" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateIpamPool", "ec2:DescribeIpamPools", "ec2:ProvisionIpamPoolCidr", "ec2:GetIpamPoolCidrs", "ec2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeIpamPools", "ec2:GetIpamPoolCidrs" ]
    },
    "update" : {
      "permissions" : [ "ec2:ModifyIpamPool", "ec2:DescribeIpamPools", "ec2:GetIpamPoolCidrs", "ec2:ProvisionIpamPoolCidr", "ec2:DeprovisionIpamPoolCidr", "ec2:CreateTags", "ec2:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteIpamPool", "ec2:DescribeIpamPools", "ec2:GetIpamPoolCidrs", "ec2:DeprovisionIpamPoolCidr", "ec2:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeIpamPools" ]
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