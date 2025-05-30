SCHEMA = {
  "typeName" : "AWS::M2::Environment",
  "description" : "Represents a runtime environment that can run migrated mainframe applications.",
  "definitions" : {
    "EfsStorageConfiguration" : {
      "type" : "object",
      "description" : "Defines the storage configuration for an Amazon EFS file system.",
      "properties" : {
        "FileSystemId" : {
          "type" : "string",
          "description" : "The file system identifier.",
          "pattern" : "^\\S{1,200}$"
        },
        "MountPoint" : {
          "type" : "string",
          "description" : "The mount point for the file system.",
          "pattern" : "^\\S{1,200}$"
        }
      },
      "required" : [ "FileSystemId", "MountPoint" ],
      "additionalProperties" : False
    },
    "EngineType" : {
      "type" : "string",
      "description" : "The target platform for the environment.",
      "enum" : [ "microfocus", "bluage" ]
    },
    "FsxStorageConfiguration" : {
      "type" : "object",
      "description" : "Defines the storage configuration for an Amazon FSx file system.",
      "properties" : {
        "FileSystemId" : {
          "type" : "string",
          "description" : "The file system identifier.",
          "pattern" : "^\\S{1,200}$"
        },
        "MountPoint" : {
          "type" : "string",
          "description" : "The mount point for the file system.",
          "pattern" : "^\\S{1,200}$"
        }
      },
      "required" : [ "FileSystemId", "MountPoint" ],
      "additionalProperties" : False
    },
    "HighAvailabilityConfig" : {
      "type" : "object",
      "description" : "Defines the details of a high availability configuration.",
      "properties" : {
        "DesiredCapacity" : {
          "type" : "integer",
          "maximum" : 100,
          "minimum" : 1
        }
      },
      "required" : [ "DesiredCapacity" ],
      "additionalProperties" : False
    },
    "NetworkType" : {
      "type" : "string",
      "enum" : [ "ipv4", "dual" ]
    },
    "StorageConfiguration" : {
      "type" : "object",
      "description" : "Defines the storage configuration for an environment.",
      "oneOf" : [ {
        "properties" : {
          "Efs" : {
            "$ref" : "#/definitions/EfsStorageConfiguration"
          }
        },
        "required" : [ "Efs" ],
        "additionalProperties" : False
      }, {
        "properties" : {
          "Fsx" : {
            "$ref" : "#/definitions/FsxStorageConfiguration"
          }
        },
        "required" : [ "Fsx" ],
        "additionalProperties" : False
      } ]
    },
    "TagMap" : {
      "type" : "object",
      "description" : "Defines tags associated to an environment.",
      "maxProperties" : 200,
      "minProperties" : 0,
      "patternProperties" : {
        "^(?!aws:).+$" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Description" : {
      "type" : "string",
      "description" : "The description of the environment.",
      "maxLength" : 500,
      "minLength" : 0
    },
    "EngineType" : {
      "$ref" : "#/definitions/EngineType"
    },
    "EngineVersion" : {
      "type" : "string",
      "description" : "The version of the runtime engine for the environment.",
      "pattern" : "^\\S{1,10}$"
    },
    "EnvironmentArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the runtime environment.",
      "pattern" : "^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}$"
    },
    "EnvironmentId" : {
      "type" : "string",
      "description" : "The unique identifier of the environment.",
      "pattern" : "^\\S{1,80}$"
    },
    "HighAvailabilityConfig" : {
      "$ref" : "#/definitions/HighAvailabilityConfig"
    },
    "InstanceType" : {
      "type" : "string",
      "description" : "The type of instance underlying the environment.",
      "pattern" : "^\\S{1,20}$"
    },
    "KmsKeyId" : {
      "type" : "string",
      "maxLength" : 2048,
      "description" : "The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the environment.",
      "pattern" : "^[A-Za-z0-9][A-Za-z0-9_\\-]{1,59}$"
    },
    "NetworkType" : {
      "$ref" : "#/definitions/NetworkType"
    },
    "PreferredMaintenanceWindow" : {
      "type" : "string",
      "description" : "Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.",
      "pattern" : "^\\S{1,50}$"
    },
    "PubliclyAccessible" : {
      "type" : "boolean",
      "description" : "Specifies whether the environment is publicly accessible."
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "description" : "The list of security groups for the VPC associated with this environment.",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^\\S{1,50}$"
      }
    },
    "StorageConfigurations" : {
      "type" : "array",
      "description" : "The storage configurations defined for the runtime environment.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/StorageConfiguration"
      }
    },
    "SubnetIds" : {
      "type" : "array",
      "description" : "The unique identifiers of the subnets assigned to this runtime environment.",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^\\S{1,50}$"
      }
    },
    "Tags" : {
      "description" : "Tags associated to this environment.",
      "$ref" : "#/definitions/TagMap"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "m2:TagResource", "m2:UntagResource", "m2:ListTagsForResource" ]
  },
  "required" : [ "EngineType", "InstanceType", "Name" ],
  "readOnlyProperties" : [ "/properties/EnvironmentArn", "/properties/EnvironmentId" ],
  "createOnlyProperties" : [ "/properties/Description", "/properties/EngineType", "/properties/KmsKeyId", "/properties/Name", "/properties/NetworkType", "/properties/PubliclyAccessible", "/properties/SecurityGroupIds", "/properties/StorageConfigurations", "/properties/SubnetIds" ],
  "primaryIdentifier" : [ "/properties/EnvironmentArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateNetworkInterface", "ec2:CreateNetworkInterfacePermission", "ec2:DescribeNetworkInterfaces", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcAttribute", "ec2:DescribeVpcs", "ec2:ModifyNetworkInterfaceAttribute", "elasticfilesystem:DescribeMountTargets", "elasticloadbalancing:CreateLoadBalancer", "elasticloadbalancing:DeleteLoadBalancer", "elasticloadbalancing:AddTags", "fsx:DescribeFileSystems", "iam:CreateServiceLinkedRole", "kms:DescribeKey", "kms:CreateGrant", "m2:CreateEnvironment", "m2:GetEnvironment", "m2:ListTagsForResource", "m2:TagResource" ],
      "timeoutInMinutes" : 120
    },
    "read" : {
      "permissions" : [ "m2:ListTagsForResource", "m2:GetEnvironment" ]
    },
    "update" : {
      "permissions" : [ "m2:TagResource", "m2:UntagResource", "m2:ListTagsForResource", "m2:GetEnvironment", "m2:UpdateEnvironment", "kms:DescribeKey" ],
      "timeoutInMinutes" : 120
    },
    "delete" : {
      "permissions" : [ "elasticloadbalancing:DeleteLoadBalancer", "m2:DeleteEnvironment", "m2:GetEnvironment" ],
      "timeoutInMinutes" : 120
    },
    "list" : {
      "permissions" : [ "m2:ListEnvironments" ]
    }
  },
  "additionalProperties" : False
}