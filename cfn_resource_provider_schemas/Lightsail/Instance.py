SCHEMA = {
  "typeName" : "AWS::Lightsail::Instance",
  "description" : "Resource Type definition for AWS::Lightsail::Instance",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
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
      "required" : [ "Key" ],
      "additionalProperties" : False
    },
    "ipv6Cidrs" : {
      "description" : "IPv6 Cidrs",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "cidrs" : {
      "description" : "cidrs",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "cidrListAliases" : {
      "description" : "cidr List Aliases",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "AutoSnapshotAddOn" : {
      "description" : "An object that represents additional parameters when enabling or modifying the automatic snapshot add-on",
      "type" : "object",
      "properties" : {
        "SnapshotTimeOfDay" : {
          "type" : "string",
          "description" : "The daily time when an automatic snapshot will be created.",
          "pattern" : "^[0-9]{2}:00$"
        }
      },
      "additionalProperties" : False
    },
    "AddOn" : {
      "description" : "A addon associate with a resource.",
      "type" : "object",
      "properties" : {
        "AddOnType" : {
          "type" : "string",
          "description" : "The add-on type",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Status" : {
          "type" : "string",
          "description" : "Status of the Addon",
          "enum" : [ "Enabling", "Disabling", "Enabled", "Terminating", "Terminated", "Disabled", "Failed" ]
        },
        "AutoSnapshotAddOnRequest" : {
          "$ref" : "#/definitions/AutoSnapshotAddOn"
        }
      },
      "required" : [ "AddOnType" ],
      "additionalProperties" : False
    },
    "Location" : {
      "description" : "Location of a resource.",
      "type" : "object",
      "properties" : {
        "AvailabilityZone" : {
          "type" : "string",
          "description" : "The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request."
        },
        "RegionName" : {
          "type" : "string",
          "description" : "The Region Name in which to create your instance."
        }
      },
      "additionalProperties" : False
    },
    "Disk" : {
      "description" : "Disk associated with the Instance.",
      "type" : "object",
      "properties" : {
        "DiskName" : {
          "description" : "The names to use for your new Lightsail disk.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9][\\w\\-.]*[a-zA-Z0-9]$",
          "minLength" : 1,
          "maxLength" : 254
        },
        "SizeInGb" : {
          "type" : "string",
          "description" : "Size of the disk attached to the Instance."
        },
        "IsSystemDisk" : {
          "type" : "boolean",
          "description" : "Is the Attached disk is the system disk of the Instance."
        },
        "IOPS" : {
          "type" : "integer",
          "description" : "IOPS of disk."
        },
        "Path" : {
          "type" : "string",
          "description" : "Path of the disk attached to the instance."
        },
        "AttachedTo" : {
          "type" : "string",
          "description" : "Instance attached to the disk."
        },
        "AttachmentState" : {
          "type" : "string",
          "description" : "Attachment state of the disk."
        }
      },
      "required" : [ "DiskName", "Path" ],
      "additionalProperties" : False
    },
    "Hardware" : {
      "description" : "Hardware of the Instance.",
      "type" : "object",
      "properties" : {
        "CpuCount" : {
          "type" : "integer",
          "description" : "CPU count of the Instance."
        },
        "RamSizeInGb" : {
          "type" : "integer",
          "description" : "RAM Size of the Instance."
        },
        "Disks" : {
          "description" : "Disks attached to the Instance.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/Disk"
          }
        }
      },
      "additionalProperties" : False
    },
    "State" : {
      "description" : "Current State of the Instance.",
      "type" : "object",
      "properties" : {
        "Code" : {
          "type" : "integer",
          "description" : "Status code of the Instance."
        },
        "Name" : {
          "type" : "string",
          "description" : "Status code of the Instance."
        }
      },
      "additionalProperties" : False
    },
    "Port" : {
      "description" : "Port of the Instance.",
      "type" : "object",
      "properties" : {
        "FromPort" : {
          "type" : "integer",
          "description" : "From Port of the Instance."
        },
        "ToPort" : {
          "type" : "integer",
          "description" : "To Port of the Instance."
        },
        "Protocol" : {
          "type" : "string",
          "description" : "Port Protocol of the Instance."
        },
        "AccessFrom" : {
          "type" : "string",
          "description" : "Access From Protocol of the Instance."
        },
        "AccessType" : {
          "type" : "string",
          "description" : "Access Type Protocol of the Instance."
        },
        "CommonName" : {
          "type" : "string",
          "description" : "CommonName for Protocol of the Instance."
        },
        "AccessDirection" : {
          "type" : "string",
          "description" : "Access Direction for Protocol of the Instance(inbound/outbound)."
        },
        "Ipv6Cidrs" : {
          "$ref" : "#/definitions/ipv6Cidrs"
        },
        "CidrListAliases" : {
          "$ref" : "#/definitions/cidrListAliases"
        },
        "Cidrs" : {
          "$ref" : "#/definitions/cidrs"
        }
      },
      "additionalProperties" : False
    },
    "MonthlyTransfer" : {
      "description" : "Monthly Transfer of the Instance.",
      "type" : "object",
      "properties" : {
        "GbPerMonthAllocated" : {
          "type" : "string",
          "description" : "GbPerMonthAllocated of the Instance."
        }
      },
      "additionalProperties" : False
    },
    "Networking" : {
      "description" : "Networking of the Instance.",
      "type" : "object",
      "properties" : {
        "Ports" : {
          "description" : "Ports to the Instance.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/Port"
          }
        },
        "MonthlyTransfer" : {
          "$ref" : "#/definitions/MonthlyTransfer"
        }
      },
      "required" : [ "Ports" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "SupportCode" : {
      "description" : "Support code to help identify any issues",
      "type" : "string"
    },
    "ResourceType" : {
      "description" : "Resource type of Lightsail instance.",
      "type" : "string"
    },
    "IsStaticIp" : {
      "description" : "Is the IP Address of the Instance is the static IP",
      "type" : "boolean"
    },
    "PrivateIpAddress" : {
      "description" : "Private IP Address of the Instance",
      "type" : "string"
    },
    "PublicIpAddress" : {
      "description" : "Public IP Address of the Instance",
      "type" : "string"
    },
    "Ipv6Addresses" : {
      "description" : "IPv6 addresses of the instance",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Location" : {
      "$ref" : "#/definitions/Location"
    },
    "Hardware" : {
      "$ref" : "#/definitions/Hardware"
    },
    "State" : {
      "$ref" : "#/definitions/State"
    },
    "Networking" : {
      "$ref" : "#/definitions/Networking"
    },
    "UserName" : {
      "description" : "Username of the  Lightsail instance.",
      "type" : "string"
    },
    "SshKeyName" : {
      "description" : "SSH Key Name of the  Lightsail instance.",
      "type" : "string"
    },
    "InstanceName" : {
      "description" : "The names to use for your new Lightsail instance.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9][\\w\\-.]*[a-zA-Z0-9]$",
      "minLength" : 1,
      "maxLength" : 254
    },
    "AvailabilityZone" : {
      "description" : "The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "BundleId" : {
      "description" : "The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "BlueprintId" : {
      "description" : "The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "AddOns" : {
      "description" : "An array of objects representing the add-ons to enable for the new instance.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/AddOn"
      }
    },
    "UserData" : {
      "description" : "A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.",
      "type" : "string"
    },
    "KeyPairName" : {
      "description" : "The name of your key pair.",
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
    },
    "InstanceArn" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "InstanceName", "BlueprintId", "BundleId" ],
  "readOnlyProperties" : [ "/properties/InstanceArn", "/properties/SshKeyName", "/properties/SupportCode", "/properties/ResourceType", "/properties/IsStaticIp", "/properties/PrivateIpAddress", "/properties/PublicIpAddress", "/properties/Ipv6Addresses", "/properties/Location/AvailabilityZone", "/properties/Location/RegionName", "/properties/Hardware/CpuCount", "/properties/Hardware/RamSizeInGb", "/properties/State/Code", "/properties/State/Name", "/properties/UserName", "/properties/Networking/MonthlyTransfer/GbPerMonthAllocated" ],
  "writeOnlyProperties" : [ "/properties/UserData" ],
  "primaryIdentifier" : [ "/properties/InstanceName" ],
  "createOnlyProperties" : [ "/properties/InstanceName", "/properties/BlueprintId", "/properties/BundleId", "/properties/AvailabilityZone" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:CreateInstances", "lightsail:GetInstances", "lightsail:EnableAddOn", "lightsail:GetInstance", "lightsail:DisableAddOn", "lightsail:PutInstancePublicPorts", "lightsail:AttachDisk", "lightsail:DetachDisk", "lightsail:StartInstance", "lightsail:StopInstance", "lightsail:GetDisk", "lightsail:GetRegions", "lightsail:TagResource", "lightsail:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetInstances", "lightsail:GetInstance" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:GetInstances", "lightsail:GetInstance", "lightsail:DeleteInstance" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetInstances" ]
    },
    "update" : {
      "permissions" : [ "lightsail:GetInstances", "lightsail:GetInstance", "lightsail:DeleteInstance", "lightsail:EnableAddOn", "lightsail:DisableAddOn", "lightsail:PutInstancePublicPorts", "lightsail:AttachDisk", "lightsail:DetachDisk", "lightsail:StartInstance", "lightsail:StopInstance", "lightsail:GetDisk", "lightsail:TagResource", "lightsail:UntagResource" ],
      "timeoutInMinutes" : 2160
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "lightsail:TagResource", "lightsail:UntagResource" ]
  }
}