SCHEMA = {
  "typeName" : "AWS::SecurityHub::Insight",
  "description" : "The AWS::SecurityHub::Insight resource represents the AWS Security Hub Insight in your account. An AWS Security Hub insight is a collection of related findings.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securityhub",
  "definitions" : {
    "NonEmptyString" : {
      "description" : "Non-empty string definition.",
      "type" : "string",
      "minLength" : 1
    },
    "DateFilter" : {
      "description" : "A date filter for querying findings.",
      "properties" : {
        "DateRange" : {
          "$ref" : "#/definitions/DateRange"
        },
        "End" : {
          "$ref" : "#/definitions/ISO8601DateString"
        },
        "Start" : {
          "$ref" : "#/definitions/ISO8601DateString"
        }
      },
      "type" : "object",
      "additionalProperties" : False
    },
    "DateRange" : {
      "description" : "A date range for the date filter.",
      "properties" : {
        "Unit" : {
          "description" : "A date range unit for the date filter.",
          "enum" : [ "DAYS" ],
          "type" : "string"
        },
        "Value" : {
          "description" : "A date range value for the date filter.",
          "type" : "number"
        }
      },
      "required" : [ "Unit", "Value" ],
      "type" : "object",
      "additionalProperties" : False
    },
    "ISO8601DateString" : {
      "description" : "The date and time, in UTC and ISO 8601 format.",
      "type" : "string",
      "pattern" : "^([\\+-]?\\d{4}(?!\\d{2}))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([tT]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$"
    },
    "NumberFilter" : {
      "description" : "A number filter for querying findings.",
      "properties" : {
        "Eq" : {
          "description" : "The equal-to condition to be applied to a single field when querying for findings.",
          "type" : "number"
        },
        "Gte" : {
          "description" : "The greater-than-equal condition to be applied to a single field when querying for findings.",
          "type" : "number"
        },
        "Lte" : {
          "description" : "The less-than-equal condition to be applied to a single field when querying for findings.",
          "type" : "number"
        }
      },
      "type" : "object",
      "additionalProperties" : False
    },
    "StringFilter" : {
      "description" : "A string filter for filtering AWS Security Hub findings.",
      "properties" : {
        "Comparison" : {
          "$ref" : "#/definitions/StringFilterComparison"
        },
        "Value" : {
          "$ref" : "#/definitions/NonEmptyString"
        }
      },
      "required" : [ "Comparison", "Value" ],
      "type" : "object",
      "additionalProperties" : False
    },
    "StringFilterComparison" : {
      "description" : "The condition to apply to a string value when filtering Security Hub findings.",
      "enum" : [ "EQUALS", "PREFIX", "NOT_EQUALS", "PREFIX_NOT_EQUALS" ],
      "type" : "string"
    },
    "MapFilter" : {
      "description" : "A map filter for filtering AWS Security Hub findings.",
      "properties" : {
        "Comparison" : {
          "description" : "The condition to apply to the key value when filtering Security Hub findings with a map filter.",
          "enum" : [ "EQUALS", "NOT_EQUALS" ],
          "type" : "string"
        },
        "Key" : {
          "$ref" : "#/definitions/NonEmptyString"
        },
        "Value" : {
          "$ref" : "#/definitions/NonEmptyString"
        }
      },
      "required" : [ "Comparison", "Key", "Value" ],
      "type" : "object",
      "additionalProperties" : False
    },
    "IpFilter" : {
      "description" : "The IP filter for querying findings.",
      "properties" : {
        "Cidr" : {
          "description" : "A finding's CIDR value.",
          "$ref" : "#/definitions/NonEmptyString"
        }
      },
      "required" : [ "Cidr" ],
      "type" : "object",
      "additionalProperties" : False
    },
    "KeywordFilter" : {
      "description" : "A keyword filter for querying findings.",
      "properties" : {
        "Value" : {
          "description" : "A value for the keyword.",
          "$ref" : "#/definitions/NonEmptyString"
        }
      },
      "required" : [ "Value" ],
      "type" : "object",
      "additionalProperties" : False
    },
    "BooleanFilter" : {
      "description" : "Boolean filter for querying findings.",
      "properties" : {
        "Value" : {
          "description" : "The value of the boolean.",
          "type" : "boolean"
        }
      },
      "required" : [ "Value" ],
      "type" : "object",
      "additionalProperties" : False
    },
    "AwsSecurityFindingFilters" : {
      "description" : "A collection of filters that are applied to all active findings aggregated by AWS Security Hub.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ProductArn" : {
          "description" : "The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider's product (solution that generates findings) is registered with Security Hub.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "AwsAccountId" : {
          "description" : "The AWS account ID in which a finding is generated.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "AwsAccountName" : {
          "description" : "The name of the AWS account in which a finding is generated.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Id" : {
          "description" : "The security findings provider-specific identifier for a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "GeneratorId" : {
          "description" : "The identifier for the solution-specific component (a discrete unit of logic) that generated a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Type" : {
          "description" : "A finding type in the format of namespace/category/classifier that classifies a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Region" : {
          "description" : "The Region from which the finding was generated.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FirstObservedAt" : {
          "description" : "An ISO8601-formatted timestamp that indicates when the security findings provider first observed the potential security issue that a finding captured.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "LastObservedAt" : {
          "description" : "An ISO8601-formatted timestamp that indicates when the security findings provider most recently observed the potential security issue that a finding captured.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "CreatedAt" : {
          "description" : "An ISO8601-formatted timestamp that indicates when the security findings provider captured the potential security issue that a finding captured.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "UpdatedAt" : {
          "description" : "An ISO8601-formatted timestamp that indicates when the security findings provider last updated the finding record.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "SeverityLabel" : {
          "description" : "The label of a finding's severity.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Confidence" : {
          "description" : "A finding's confidence.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Criticality" : {
          "description" : "The level of importance assigned to the resources associated with the finding.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Title" : {
          "description" : "A finding's title.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Description" : {
          "description" : "A finding's description.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "RecommendationText" : {
          "description" : "The recommendation of what to do about the issue described in a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "SourceUrl" : {
          "description" : "A URL that links to a page about the current finding in the security findings provider's solution.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProductFields" : {
          "description" : "A data type where security findings providers can include additional solution-specific details that aren't part of the defined AwsSecurityFinding format.",
          "items" : {
            "$ref" : "#/definitions/MapFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProductName" : {
          "description" : "The name of the solution (product) that generates findings.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "CompanyName" : {
          "description" : "The name of the findings provider (company) that owns the solution (product) that generates findings.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "UserDefinedFields" : {
          "description" : "A list of name/value string pairs associated with the finding.",
          "items" : {
            "$ref" : "#/definitions/MapFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "MalwareName" : {
          "description" : "The name of the malware that was observed.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "MalwareType" : {
          "description" : "The type of the malware that was observed.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "MalwarePath" : {
          "description" : "The filesystem path of the malware that was observed.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "MalwareState" : {
          "description" : "The state of the malware that was observed.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkDirection" : {
          "description" : "Indicates the direction of network traffic associated with a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkProtocol" : {
          "description" : "The protocol of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkSourceIpV4" : {
          "description" : "The source IPv4 address of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/IpFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkSourceIpV6" : {
          "description" : "The source IPv6 address of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/IpFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkSourcePort" : {
          "description" : "The source port of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkSourceDomain" : {
          "description" : "The source domain of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkSourceMac" : {
          "description" : "The source media access control (MAC) address of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkDestinationIpV4" : {
          "description" : "The destination IPv4 address of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/IpFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkDestinationIpV6" : {
          "description" : "The destination IPv6 address of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/IpFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkDestinationPort" : {
          "description" : "The destination port of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NetworkDestinationDomain" : {
          "description" : "The destination domain of network-related information about a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProcessName" : {
          "description" : "The name of the process.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProcessPath" : {
          "description" : "The path to the process executable.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProcessPid" : {
          "description" : "The process ID.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProcessParentPid" : {
          "description" : "The parent process ID.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProcessLaunchedAt" : {
          "description" : "A timestamp that identifies when the process was launched.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ProcessTerminatedAt" : {
          "description" : "A timestamp that identifies when the process was terminated.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ThreatIntelIndicatorType" : {
          "description" : "The type of a threat intelligence indicator.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ThreatIntelIndicatorValue" : {
          "description" : "The value of a threat intelligence indicator.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ThreatIntelIndicatorCategory" : {
          "description" : "The category of a threat intelligence indicator.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ThreatIntelIndicatorLastObservedAt" : {
          "description" : "A timestamp that identifies the last observation of a threat intelligence indicator.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ThreatIntelIndicatorSource" : {
          "description" : "The source of the threat intelligence.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ThreatIntelIndicatorSourceUrl" : {
          "description" : "The URL for more details from the source of the threat intelligence.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceType" : {
          "description" : "Specifies the type of the resource that details are provided for.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceId" : {
          "description" : "The canonical identifier for the given resource type.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourcePartition" : {
          "description" : "The canonical AWS partition name that the Region is assigned to.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceRegion" : {
          "description" : "The canonical AWS external Region name where this resource is located.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceTags" : {
          "description" : "A list of AWS tags associated with a resource at the time the finding was processed.",
          "items" : {
            "$ref" : "#/definitions/MapFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceType" : {
          "description" : "The instance type of the instance.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceImageId" : {
          "description" : "The Amazon Machine Image (AMI) ID of the instance.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceIpV4Addresses" : {
          "description" : "The IPv4 addresses associated with the instance.",
          "items" : {
            "$ref" : "#/definitions/IpFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceIpV6Addresses" : {
          "description" : "The IPv6 addresses associated with the instance.",
          "items" : {
            "$ref" : "#/definitions/IpFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceKeyName" : {
          "description" : "The key name associated with the instance.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceIamInstanceProfileArn" : {
          "description" : "The IAM profile ARN of the instance.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceVpcId" : {
          "description" : "The identifier of the VPC that the instance was launched in.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceSubnetId" : {
          "description" : "The identifier of the subnet that the instance was launched in.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsEc2InstanceLaunchedAt" : {
          "description" : "The date and time the instance was launched.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsS3BucketOwnerId" : {
          "description" : "The canonical user ID of the owner of the S3 bucket.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsS3BucketOwnerName" : {
          "description" : "The display name of the owner of the S3 bucket.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsIamAccessKeyStatus" : {
          "description" : "The status of the IAM access key related to a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsIamAccessKeyCreatedAt" : {
          "description" : "The creation date/time of the IAM access key related to a finding.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceContainerName" : {
          "description" : "The name of the container related to a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceContainerImageId" : {
          "description" : "The identifier of the image related to a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceContainerImageName" : {
          "description" : "The name of the image related to a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceContainerLaunchedAt" : {
          "description" : "A timestamp that identifies when the container was started.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceDetailsOther" : {
          "description" : "The details of a resource that doesn't have a specific subfield for the resource type defined.",
          "items" : {
            "$ref" : "#/definitions/MapFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ComplianceStatus" : {
          "description" : "Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "VerificationState" : {
          "description" : "The veracity of a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "WorkflowState" : {
          "description" : "The workflow state of a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "WorkflowStatus" : {
          "description" : "The status of the investigation into a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "RecordState" : {
          "description" : "The updated record state for the finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "RelatedFindingsProductArn" : {
          "description" : "The ARN of the solution that generated a related finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "RelatedFindingsId" : {
          "description" : "The solution-generated identifier for a related finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceApplicationArn" : {
          "description" : "The ARN of the application that is related to a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceApplicationName" : {
          "description" : "The name of the application that is related to a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NoteText" : {
          "description" : "The text of a note.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NoteUpdatedAt" : {
          "description" : "The timestamp of when the note was updated.",
          "items" : {
            "$ref" : "#/definitions/DateFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "NoteUpdatedBy" : {
          "description" : "The principal that created a note.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Sample" : {
          "description" : "Indicates whether or not sample findings are included in the filter results.",
          "items" : {
            "$ref" : "#/definitions/BooleanFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ComplianceAssociatedStandardsId" : {
          "description" : "The unique identifier of a standard in which a control is enabled.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ComplianceSecurityControlId" : {
          "description" : "The unique identifier of a control across standards.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ComplianceSecurityControlParametersName" : {
          "description" : "The name of a security control parameter.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ComplianceSecurityControlParametersValue" : {
          "description" : "The current value of a security control parameter.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FindingProviderFieldsConfidence" : {
          "description" : "The finding provider value for the finding confidence.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FindingProviderFieldsCriticality" : {
          "description" : "The finding provider value for the level of importance assigned to the resources associated with the findings.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FindingProviderFieldsRelatedFindingsId" : {
          "description" : "The finding identifier of a related finding that is identified by the finding provider.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FindingProviderFieldsRelatedFindingsProductArn" : {
          "description" : "The ARN of the solution that generated a related finding that is identified by the finding provider.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FindingProviderFieldsSeverityLabel" : {
          "description" : "The finding provider value for the severity label.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FindingProviderFieldsSeverityOriginal" : {
          "description" : "The finding provider's original value for the severity.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "FindingProviderFieldsTypes" : {
          "description" : "One or more finding types that the finding provider assigned to the finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsIamAccessKeyPrincipalName" : {
          "description" : "The name of the principal that is associated with an IAM access key.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsIamUserUserName" : {
          "description" : "The name of an IAM user.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "VulnerabilitiesExploitAvailable" : {
          "description" : "Indicates whether a software vulnerability in your environment has a known exploit.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "VulnerabilitiesFixAvailable" : {
          "description" : "Indicates whether a vulnerability is fixed in a newer version of the affected software packages.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "Keyword" : {
          "description" : "A keyword for a finding.",
          "items" : {
            "$ref" : "#/definitions/KeywordFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "ResourceAwsIamAccessKeyUserName" : {
          "description" : "The user associated with the IAM access key related to a finding.",
          "items" : {
            "$ref" : "#/definitions/StringFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "SeverityNormalized" : {
          "description" : "The normalized severity of a finding.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        },
        "SeverityProduct" : {
          "description" : "The native severity as defined by the security findings provider's solution that generated the finding.",
          "items" : {
            "$ref" : "#/definitions/NumberFilter"
          },
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : True,
          "maxItems" : 20
        }
      }
    }
  },
  "properties" : {
    "InsightArn" : {
      "description" : "The ARN of a Security Hub insight",
      "type" : "string",
      "pattern" : "arn:aws\\S*:securityhub:\\S*"
    },
    "Name" : {
      "description" : "The name of a Security Hub insight",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Filters" : {
      "description" : "One or more attributes used to filter the findings included in the insight",
      "$ref" : "#/definitions/AwsSecurityFindingFilters",
      "maxProperties" : 10
    },
    "GroupByAttribute" : {
      "description" : "The grouping attribute for the insight's findings",
      "$ref" : "#/definitions/NonEmptyString"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Filters", "Name", "GroupByAttribute" ],
  "primaryIdentifier" : [ "/properties/InsightArn" ],
  "readOnlyProperties" : [ "/properties/InsightArn" ],
  "deprecatedProperties" : [ "/properties/Filters/Keyword", "/properties/Filters/ResourceAwsIamAccessKeyUserName", "/properties/Filters/SeverityNormalized", "/properties/Filters/SeverityProduct" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:CreateInsight" ]
    },
    "read" : {
      "permissions" : [ "securityhub:GetInsights" ]
    },
    "update" : {
      "permissions" : [ "securityhub:UpdateInsight" ]
    },
    "delete" : {
      "permissions" : [ "securityhub:GetInsights", "securityhub:DeleteInsight" ]
    },
    "list" : {
      "permissions" : [ "securityhub:GetInsights" ]
    }
  }
}